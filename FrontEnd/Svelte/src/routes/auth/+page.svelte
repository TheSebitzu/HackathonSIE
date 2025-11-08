<script lang="ts">
  import { onMount } from "svelte";

  let mode = "login"; // "login" or "register"
  let error = "";

  // Variabile pentru ambele moduri
  let username = "";
  let password = "";

  // Variabile doar pentru register
  let email = "";
  let nume = "";
  let prenume = "";
  let telefon = "";

  const login = async () => {
    error = "";
    try {
      const res = await fetch("http://localhost:8000/api/token/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
      });

      if (res.ok) {
        const data = await res.json();
        localStorage.setItem("access_token", data.access);
        localStorage.setItem("refresh_token", data.refresh);
        window.location.href = "/pwa/Tasks"; 
      } else {
        error = "Nume de utilizator sau parolă invalidă";
      }
    } catch (e) {
      error = "Eroare de rețea. Verifică dacă serverul rulează.";
    }
  };

  const register = async () => {
    error = "";
    try {
      const res = await fetch("http://localhost:8000/api/register/", { 
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username,
          email,
          password,
          nume,
          prenume,
          telefon,
          manager: null 
        })
      });

      if (res.ok) {
        alert("Cont creat cu succes! Te poți loga acum.");
        mode = "login"; 
        
        username = "";
        password = "";
        email = "";
        nume = "";
        prenume = "";
        telefon = "";
      } else {
        const data = await res.json();
        error = Object.entries(data).map(([key, value]) => `${key}: ${value}`).join(', ');
      }
    } catch (e) {
      error = "Eroare de rețea. Verifică dacă serverul rulează.";
    }
  };

  const toggleMode = () => {
    mode = mode === "login" ? "register" : "login";
    error = "";
    username = "";
    password = "";
  };
</script>

<link href="https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap" rel="stylesheet">


<div class="tot">
  <h1>{mode === "login" ? "Login" : "Register"}</h1>

  <div class="form">

    {#if mode === 'login'}
      <input placeholder="Username" bind:value={username} />
      <input type="password" placeholder="Password" bind:value={password} />
    
    {:else}
      <input placeholder="Username (ex: ionpopescu)" bind:value={username} />
      <input placeholder="Nume (ex: Popescu)" bind:value={nume} />
      <input placeholder="Prenume (ex: Ion)" bind:value={prenume} />
      <input placeholder="Email (ex: ion@popescu.com)" type="email" bind:value={email} />
      <input placeholder="Telefon (opțional)" bind:value={telefon} />
      <input type="password" placeholder="Password" bind:value={password} />
    {/if}

    <button on:click={mode === "login" ? login : register}>
      {mode === "login" ? "Login" : "Register"}
    </button>

    <p class="error">{error}</p>

    <p class="toggle">
      {mode === "login" ? "Nu ai cont? " : "Ai deja cont? "}
      <a href="#" on:click|preventDefault={toggleMode}>
        {mode === "login" ? "Înregistrează-te" : "Intră în cont"}
      </a>
    </p>
  </div>
</div>

<style>
  /* Global reset pentru a umple tot ecranul */
  :global(html, body) {
    margin: 0;
    padding: 0;
    height: 100%;
  }

  .tot{
    background-color: #93cfdf; /* Fundalul albastru */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center; /* AICI ERA TYPO-UL 'ce' */
    min-height: 100vh; /* Asta îl face să umple ecranul */
    width: 100vw;
    padding: 1rem;
    box-sizing: border-box;
  }

  h1 {
    text-align: center;
    font-size: 2rem;
    margin: 2rem 0;
    font-family: "Momo Trust Display", sans-serif;
    color: #00246B;
  }

    input::placeholder,
  textarea::placeholder {
    font-family: 'Roboto Mono', monospace; 
    font-size: 1rem;                        
    font-style: italic;                      
    color: #888;                            
  }

  .form {
    display: flex;
    flex-direction: column;
    align-items: center;
    /* margin-top: 50vh; <- ACEASTĂ LINIE STRICA CENTRAREA */
    gap: 0.75rem;
    width: 320px;
    max-width: 100%;
    margin: 0; /* Centrarea e făcută de .tot */
    background: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }

  input {
    width: 100%;
    padding: 0.6rem;
    border-radius: 10px;
    border: 1px solid #ccc;
    font-size: 1rem;
    box-sizing: border-box;
  }

  button {
    width: 100%;
    padding: 0.7rem;
    border-radius: 12px;
    border: none;
    background-color: #53d2f2;
    color: black;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  button:hover {
    background-color: #3ac0e1;
  }

  .error {
    color: red;
    font-weight: bold;
    margin-top: 0.5rem;
    text-align: center;
  }

  .toggle {
    text-align: center;
    margin-top: 1rem;
  }

  .toggle a {
    color: #53d2f2;
    cursor: pointer;
    text-decoration: underline;
    font-weight: bold;
  }
</style>