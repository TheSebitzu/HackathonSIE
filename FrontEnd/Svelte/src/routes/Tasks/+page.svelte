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
      // Scoate task-ul din array-ul local
      tasks = tasks.filter(task => task.id !== taskId);
    } else {
      const error = await res.json();
      console.error("Error deleting task:", error);
      alert("Failed to delete task.");
    }
  };

  // Optional: format date nicely
  const formatDate = (dateStr) => {
    if (!dateStr) return "-";
    const d = new Date(dateStr);
    return d.toLocaleDateString();
  };

  // Mark task as completed
  const completeTask = async (task) => {
  try {
    const res = await fetch(`http://localhost:8000/api/tasks/${task.id}/`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ status: "completed" })
    });

    if (res.ok) {
      // Update status local
      task.status = "completed";

      // Important: trigger Svelte reactivity
      tasks = [...tasks]; // creează un nou array
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

<h1>My Tasks</h1>

<div class="task-list">
  {#each tasks as task (task.id)}
    <div class="task-card">
      <h2>{task.title}</h2>
      <p><strong>Description:</strong> {task.description || "No description"}</p>
      <p><strong>Start:</strong> {formatDate(task.start_time)}</p>
      <p><strong>End:</strong> {formatDate(task.end_time)}</p>
      <p><strong>Status:</strong> {task.status || "Unassigned"}</p>
      {#if task.status !== "completed"}
        <button class="complete-btn" on:click={() => completeTask(task)}>Complete Task</button>
      {/if}
      <button class="delete-btn" on:click={() => deleteTask(task.id)}>Delete</button>
    </div>
  {/each}
</div>

<style>
  h1 {
    margin-left: 10vh;
    margin-top: 2rem;
  }

  .task-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin: 2rem 10vh;
  }

  .task-card {
    padding: 1rem;
    border: 2px solid #ccc;
    border-radius: 10px;
    background-color: #f9f9f9;
  }

  .task-card h2 {
    margin: 0 0 0.5rem 0;
  }

  .task-card p {
    margin: 0.2rem 0;
  }

  .complete-btn {
    margin-top: 0.5rem;
    padding: 0.4rem 0.8rem;
    border-radius: 5px;
    background-color: #5cb85c;
    color: white;
    border: none;
    cursor: pointer;
  }

  .delete-btn {
    padding: 0.3rem 0.6rem;
    background-color: #d9534f;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
</style>
