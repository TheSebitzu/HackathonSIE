<script>
  import { onMount } from "svelte";

  let tasks = [];

  onMount(async () => {
    const res = await fetch("http://localhost:8000/api/tasks/");
    tasks = await res.json();
  });

  const deleteTask = async (taskId) => {
    if (!confirm("Are you sure you want to delete this task?")) return;

    const res = await fetch(`http://localhost:8000/api/tasks/${taskId}/`, {
      method: "DELETE",
    });

    if (res.ok) {
      tasks = tasks.filter(task => task.id !== taskId);
    } else {
      const error = await res.json();
      console.error("Error deleting task:", error);
      alert("Failed to delete task.");
    }
  };

  const formatDate = (dateStr) => {
    if (!dateStr) return "-";
    const d = new Date(dateStr);
    return d.toLocaleDateString();
  };

  const completeTask = async (task) => {
    try {
      const res = await fetch(`http://localhost:8000/api/tasks/${task.id}/`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ status: "completed" })
      });

      if (res.ok) {
        task.status = "completed";
        tasks = [...tasks]; 
      } else {
        const error = await res.json();
        console.error("Error completing task:", error);
        alert("Failed to complete task.");
      }
    } catch (err) {
      console.error("Network error:", err);
      alert("Network error while completing task.");
    }
  };
</script>

<div class="page-container">
  <h1>My Tasks</h1>

  <div class="task-list">
    {#each tasks as task (task.id)}
      <div class="task-card">
        <h2>{task.title}</h2>
        <p><strong>Description:</strong> {task.description || "No description"}</p>
        <p><strong>Start:</strong> {formatDate(task.start_time)}</p>
        <p><strong>End:</strong> {formatDate(task.end_time)}</p>
        <p><strong>Status:</strong> {task.status || "Unassigned"}</p>
        
        <div class="button-row">
          {#if task.status !== "completed"}
            <button class="complete-btn" on:click={() => completeTask(task)}>Complete Task</button>
          {/if}
          <button class="delete-btn" on:click={() => deleteTask(task.id)}>Delete</button>
        </div>
      </div>
    {/each}
  </div>
</div>

<style>
  /* STILURI NOI PENTRU A SE POTRIVI CU TEMA */
  :global(html, body) {
    margin: 0;
    padding: 0;
  }

  .page-container {
    background-color: #93cfdf; /* Același fundal ca la login */
    min-height: 100vh;
    width: 100%;
    padding: 1rem;
    box-sizing: border-box;
    /* Adăugăm padding jos pentru a nu se suprapune cu nav-ul de jos */
    padding-bottom: 100px; 
  }

  h1 {
    text-align: center;
    font-size: 2rem;
    margin: 2rem 0;
    font-family: "Momo Trust Display", sans-serif;
    color: #00246B;
  }

  .task-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 800px;
    margin: 0 auto; /* Centrează lista */
  }

  .task-card {
    padding: 1rem 1.5rem;
    border: none;
    border-radius: 10px;
    background-color: #f9f9f9;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Umbră ca la login */
  }
  /* ... RESTUL STILURILOR ... */

  .task-card h2 {
    margin: 0 0 0.5rem 0;
  }

  .task-card p {
    margin: 0.2rem 0;
  }

  .button-row {
    display: flex;
    gap: 0.5rem;
    margin-top: 1rem;
  }

  .complete-btn {
    padding: 0.4rem 0.8rem;
    border-radius: 5px;
    background-color: #5cb85c;
    color: white;
    border: none;
    cursor: pointer;
    font-weight: bold;
  }

  .delete-btn {
    padding: 0.4rem 0.8rem;
    background-color: #d9534f;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
  }
</style>