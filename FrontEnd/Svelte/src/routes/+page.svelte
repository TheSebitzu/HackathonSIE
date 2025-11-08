<script>
  // Importăm 'goto' pentru navigare programatică
  import { goto } from '$app/navigation';

  function goToSignUp() {
    // Asigură-te că ai un fișier src/routes/signup/+page.svelte
    goto('/auth');
  }
</script>

<div class="container">
  <h1><b>Task Manager</b></h1>

  <div class="button-group">
    <button class="btn no" on:click={goToSignUp}>
      Login
    </button>
  </div>
</div>

<style>
  .container {
    background-color: #CADCFC;
    
    /* === MODIFICAT === */
    /* Folosim unități de viewport în loc de procente */
    height: 100vh; /* 100% din înălțimea ecranului */
    width: 100vw;  /* 100% din lățimea ecranului */
    /* ================= */
    
    /* Restul codului tău de flexbox este perfect */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }

  h1 {
    font-size: 3rem;
    color: #333;
    margin-bottom: 2rem;
  }
  .button-group {
    display: flex;
    gap: 1rem;
  }
  .btn {
    padding: 0.8rem 1.5rem;
    font-size: 1.2rem;
    font-weight: bold;
    color: white;
    border: none;
    border-radius: 8px; 
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .btn.no {
    background-color: #f44336; /* A red color */
  }
  .btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
</style>