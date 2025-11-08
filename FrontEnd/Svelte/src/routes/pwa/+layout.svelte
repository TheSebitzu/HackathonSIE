<script>
  import { page } from '$app/stores';
  import { onMount } from 'svelte';
  import { authToken, logout } from '$lib/authStore.js';

  onMount(() => {
    const token = localStorage.getItem('access_token');
    authToken.set(token);
  });
</script>

<div class="page-layout">
  <main>
    <slot />
  </main>

  <nav>
    <a href="/pwa/addTask" class:active={$page.url.pathname === '/pwa/addTask'}>
      <div class="titlu"><p id="t">Adaugare</p><p id="m">Task</p></div>
    </a>
    <a href="/pwa/Tasks" class:active={$page.url.pathname === '/pwa/Tasks'}>
      <div class="titlu"><p id="t">Taskurile</p><p id="m">Mele</p></div>
    </a>
    <a href="/pwa/Groups" class:active={$page.url.pathname === '/pwa/Groups'}>
      <div class="titlu"><p id="t">Grupurile</p><p id="m">Mele</p></div>
    </a>
    <a href="#" on:click|preventDefault={logout}>
       <div class="titlu">
        <p id="t">Ieșire</p>
        <p id="m">Cont</p>
      </div>
    </a>
  </nav>
</div>

<style>
.page-layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100%;
  overflow-x: hidden;
}

main {
  flex: 1;
  overflow-y: auto;
}

.titlu{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
#t,#m{
  margin: 2px;
}

nav {
  flex-shrink: 0;
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 1rem;
  background-color: #00246B;
  border-top: 1px solid rgb(64, 226, 235);
}

nav a {
  text-decoration: none;
  color: #d3d0f4;
  font-size: 1rem;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  width: 100%;
  font-family: sans-serif;
  font-weight: bold;
  transition: background-color 0.2s;
}

nav a.active {
  background-color: #007bff;
  color: white;
}

:global(body) {
  margin: 0;
  overflow-x: hidden;
}

:global(.container), :global(.container-next) {
  min-height: 100%;
  width: 100%;
  margin: 0;
  box-sizing: border-box; 
}
</style>
