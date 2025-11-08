<script lang="ts">
  import { onMount } from 'svelte';

  // Tipurile
  type User = { id: number; name: string };
  type Task = { id: number; title: string };
  type Group = {
    id: number;
    name: string;
    members: string[];
    expanded: boolean;
    task_title: string;
  };

  // Grupurile existente
  let groups: Group[] = [];

  // Form creare grup
  let showCreateForm = false;
  let users: User[] = [];
  let tasks: Task[] = [];
  let groupName = '';
  let selectedUserIds: number[] = [];
  let selectedTaskId: number | null = null;

  async function loadGroups() {
    const res = await fetch('/api/grupuri/');
    if (res.ok) {
      const data = await res.json();
      groups = data.map((g: any) => ({ ...g, expanded: false }));
    }
  }

  async function loadUsersTasks() {
    const res = await fetch('/api/users-tasks/');
    if (res.ok) {
      const data = await res.json();
      users = data.users;
      tasks = data.tasks;
    }
  }

  onMount(() => {
    loadGroups();
    loadUsersTasks();
  });

  function toggleDropdown(group: Group) {
    groups = groups.map(g =>
      g.id === group.id ? { ...g, expanded: !g.expanded } : g
    );
  }

  function removeMember(group: Group, member: string) {
    if (confirm(`Elimini ${member} din ${group.name}?`)) {
      groups = groups.map(g =>
        g.id === group.id ? { ...g, members: g.members.filter(m => m !== member) } : g
      );
    }
  }

  async function createGroup() {
    if (!groupName || selectedUserIds.length === 0) {
      alert("Completează toate câmpurile!");
      return;
    }

    const res = await fetch('/api/groups/create/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: groupName,
        member_ids: selectedUserIds,
        task_id: selectedTaskId
      })
    });

    if (res.ok) {
      alert('Grup creat cu succes!');
      showCreateForm = false;
      groupName = '';
      selectedUserIds = [];
      selectedTaskId = null;
      await loadGroups();
    } else {
      alert('Eroare la crearea grupului.');
    }
  }
</script>

<div class="page-layout">
  <h1>Grupurile Mele</h1>

  <button class="add-btn" on:click={() => showCreateForm = true}>➕ Creează Grup</button>

  {#each groups as group (group.id)}
    <div class="group-card">
      <button class="group-header" on:click={() => toggleDropdown(group)}>
        <div>
          <h2>{group.name}</h2>
          <p class="task-title">{group.task_title}</p>
        </div>
        <span class="arrow">{group.expanded ? "▲" : "▼"}</span>
      </button>

      {#if group.expanded}
        <div class="group-content">
          <ul>
            {#each group.members as member}
              <li>
                {member}
                <button class="remove-btn" on:click={() => removeMember(group, member)}>✖</button>
              </li>
            {/each}
          </ul>
        </div>
      {/if}
    </div>
  {/each}

  {#if showCreateForm}
    <div class="modal">
      <div class="modal-content">
        <h2>Creează Grup Nou</h2>
        <input type="text" placeholder="Nume grup" bind:value={groupName} />

        <h3>Selectează membri:</h3>
        {#each users as user}
          <label>
            <input type="checkbox" bind:group={selectedUserIds} value={user.id} />
            {user.name}
          </label>
        {/each}

        {#if selectedUserIds.length > 0}
          <p><strong>Membri selectați:</strong> 
            {selectedUserIds.map(id => users.find(u => u.id === id)?.name).join(", ")}
          </p>
        {/if}

        <h3>Selectează task:</h3>
        <select bind:value={selectedTaskId}>
          <option value={null}>Selectează task</option>
          {#each tasks as task}
            <option value={task.id}>{task.title}</option>
          {/each}
        </select>

        <button class="add-btn" on:click={createGroup}>Creează</button>
        <button class="remove-btn" on:click={() => showCreateForm = false}>Închide</button>
      </div>
    </div>
  {/if}
</div>

<style>
.page-layout {
  min-height: 100vh;
  background-color: rgb(145, 221, 221);
  padding: 2rem;
  box-sizing: border-box;
  font-family: "Momo Trust Display", sans-serif;
}

h1 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 1rem;
}

.add-btn {
  background-color: #53d2f2;
  color: black;
  font-weight: bold;
  border: none;
  border-radius: 12px;
  padding: 0.6rem 1rem;
  cursor: pointer;
  margin-bottom: 1rem;
}

.add-btn:hover {
  background-color: #3ac0e1;
}

.group-card {
  background: white;
  border-radius: 20px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  margin: 1rem auto;
  padding: 1rem 1.5rem;
  max-width: 600px;
  transition: transform 0.2s ease;
}

.group-card:hover {
  transform: scale(1.02);
}

.group-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: none;
  border: none;
  width: 100%;
  cursor: pointer;
  padding: 0.5rem 1rem;
  font: inherit;
}

.group-header h2 {
  margin: 0;
}

.task-title {
  margin: 0.2rem 0 0 0;
  font-size: 0.9rem;
  color: #555;
}

.arrow {
  font-size: 1.2rem;
}

.group-content {
  margin-top: 1rem;
  padding-top: 0.5rem;
  border-top: 1px solid #ccc;
}

ul {
  list-style: none;
  padding-left: 0;
  margin: 0.5rem 0 1rem 0;
}

li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f9f9f9;
  border-radius: 10px;
  padding: 0.5rem 1rem;
  margin-bottom: 0.5rem;
}

.remove-btn {
  background: transparent;
  border: none;
  color: red;
  cursor: pointer;
  font-size: 1rem;
  transition: color 0.2s;
}

.remove-btn:hover {
  color: darkred;
}

.modal {
  position: fixed;
  inset: 0;
  background-color: rgba(0,0,0,0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 2rem;
  border-radius: 20px;
  max-width: 500px;
  width: 90%;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>