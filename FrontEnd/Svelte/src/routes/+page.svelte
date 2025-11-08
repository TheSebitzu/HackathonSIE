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
    background-color: #CADCFC; /* A pink color */
    height: 100%; /* 100% of the viewport height */
    width: 100%; /* 100% of the viewport width */
    
    /* Folosim flexbox pentru a centra conținutul perfect */
    display: flex;
    flex-direction: column; /* Aliniază elementele vertical */
    justify-content: center; /* Centrează vertical */
    align-items: center; /* Centrează orizontal */
    
    /* Setăm fontul pentru lizibilitate */
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }

  /* Stilizăm titlul */
  h1 {
    font-size: 3rem; /* 3 times the base font size */
    color: #333;
    margin-bottom: 2rem; /* Spațiu sub titlu */
  }

  /* Container pentru a ține butoanele unul lângă altul */
  .button-group {
    display: flex;
    gap: 1rem; /* Adaugă spațiu de 1rem între butoane */
  }
  .btn {
    padding: 0.8rem 1.5rem;
    font-size: 1.2rem;
    font-weight: bold;
    color: white;
    border: none;
    border-radius: 8px; /* Colțuri rotunjite */
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .btn.no {
    background-color: #f44336; /* A red color */
  }
  .btn:hover {
    transform: translateY(-2px); /* Ridică ușor butonul */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Adaugă umbră */
  }
</style>