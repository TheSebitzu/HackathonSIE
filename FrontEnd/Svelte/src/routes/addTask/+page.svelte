<script>
  
  import Task from "../../components/Task.svelte";
  import { onMount } from "svelte";

  let tasks = [];

  let title = "";
  let description = "";
  let start_time = "";
  let end_time = "";
  let status = "unassigned"; // <-- add this

  const fetchTasks = async () => {
    const res = await fetch("http://localhost:8000/api/tasks/");
    tasks = await res.json();
  };

  onMount(fetchTasks);

  const addTask = async () => {
    if (!title || !start_time || !end_time) return;

    // Format date for Django
    const start = new Date(start_time).toISOString();
    const end = new Date(end_time).toISOString();

    const res = await fetch("http://localhost:8000/api/tasks/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title,
        description,
        start_time: start,
        end_time: end,
        is_finished: false,
        status // <-- include the status
      })
    });

    if (res.ok) {
      const newTask = await res.json();
      tasks = [newTask, ...tasks];
      title = description = start_time = end_time = "";
      status = "unassigned"; // reset
    } else {
      const error = await res.json();
      console.error("Error adding task:", error);
      alert("Failed to add task. Check console for details.");
    }
  };
</script>

<div class="tot">
  
  <div class="formular">
      <h1 class="h">Task nou</h1>

    <form class="formularMic" on:submit|preventDefault={addTask}>
      <div class="c">
      <div class="Campuri">Titlu</div>
      <input type="text" bind:value={title} placeholder="Title" required />
      </div>

      <div class="c">
      <div class="Campuri">Descriere</div>
        <input type="text" bind:value={description} placeholder="Description" />
    </div>
    <div class="c">
      <div class="Campuri">Data inceperii</div>
        <input type="date" bind:value={start_time} required />
    </div>
  <div class="c">

      <div class="Campuri">Data finalizarii</div>
        <input type="date" bind:value={end_time} required />
  </div>
<div class="c">

      <div class="Campuri">Status</div>
        <select bind:value={status}>
          <option value="in_progress">In Progress</option>
          <option value="assigned">Assigned</option>
          <option value="completed">Completed</option>
          <option value="unassigned">Unassigned</option>
        </select>
</div>
  <div class="c">
  <button id="sub" type="submit">Add Task</button>
  </div>
  
</form>
</div>
</div>
<style>
 
 :global(html), :global(body) {
  height: 100%;
  margin: 0;
  padding: 0;
  overflow: hidden;
  font-family: "Momo Trust Display", sans-serif;
}

.h{
  display: flex;
  align-items: center;
  justify-content: center;;
  margin-left: 3vh;
}
.tot {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;       
  height: 100%;     
  overflow-x: hidden;
  background-color: rgb(145,221,221); /* culoare exemplu */
}

/* Formularul centrat */
.formular {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  position: relative;
  background-color: whitesmoke;
  border-radius: 40px;
  min-height: 60vh; 
  min-width: 40vh;/* nu ocupă tot ecranul, dar e centrat */
  z-index: 1;
  
}

.formularMic{
  margin-left: 3vh;

}

.c{
    margin-bottom: 3vh;
}

#sub{
margin-left: 5%;
background-color: rgb(173, 227, 227);
border: 5px;
background-color: rgb(173, 227, 227);
border-radius: 5px;

}

</style>
