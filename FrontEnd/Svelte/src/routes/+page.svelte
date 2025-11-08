<div class="container">
  <!-- Titlul paginii -->
  <h1><b>Task Manager</b></h1>

  <!-- Container pentru butoane -->
  <div class="button-group">
    <button class="btn yes">Login</button>
    <button class="btn no">Sign Up</button>
  </div>
</div>

<!-- 
  Blocul <style> este specific Svelte.
  CSS-ul de aici se aplică DOAR acestui component.
-->
<style>
  /* Selectează containerul principal și îi setează
    fundalul roz și îl face să ocupe tot ecranul.
  */
  .container {
    background-color: #6df3fa; /* A pink color */
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

  /* Stil de bază pentru butoane */
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

  /* Stil pentru butonul "yes" */
  .btn.yes {
    background-color: #4caf50; /* A green color */
  }

  /* Stil pentru butonul "no" */
  .btn.no {
    background-color: #f44336; /* A red color */
  }

  /* Efect la hover pentru butoane */
  .btn:hover {
    transform: translateY(-2px); /* Ridică ușor butonul */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Adaugă umbră */
  }
</style>