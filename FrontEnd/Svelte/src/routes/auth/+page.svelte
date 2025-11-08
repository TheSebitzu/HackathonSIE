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
  // 'manager' îl vom trimite ca 'null' deocamdată,
  // dacă nu ai un câmp în formular pentru el.

  /**
   * 1. Funcția de LOGIN
   * Contactează /api/token/ cu username și password.
   */
  const login = async () => {
    error = "";
    try {
      const res = await fetch("http://localhost:8000/api/token/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }) // Login se face cu username
      });

      if (res.ok) {
        const data = await res.json();
        localStorage.setItem("access_token", data.access);
        localStorage.setItem("refresh_token", data.refresh);
        window.location.href = "/pwa/Tasks"; // Redirecționează către pagina de task-uri
      } else {
        error = "Nume de utilizator sau parolă invalidă";
      }
    } catch (e) {
      error = "Eroare de rețea. Verifică dacă serverul rulează.";
    }
  };

  /**
   * 2. Funcția de REGISTER
   * Contactează /api/register/ cu toate detaliile.
   */
  const register = async () => {
    error = "";
    try {
      const res = await fetch("http://localhost:8000/api/register/", { // URL-ul corectat cu /api/
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username,
          email,
          password,
          nume,
          prenume,
          telefon,
          manager: null // Trimite 'null' dacă nu ai un câmp pentru 'manager'
        })
      });

      if (res.ok) {
        alert("Cont creat cu succes! Te poți loga acum.");
        mode = "login"; // Comută automat pe modul login
        
        // Golește câmpurile de register
        username = "";
        password = "";
        email = "";
        nume = "";
        prenume = "";
        telefon = "";
      } else {
        // Afișează eroarea primită de la server (ex. "username already exists")
        const data = await res.json();
        error = Object.entries(data).map(([key, value]) => `${key}: ${value}`).join(', ');
      }
    } catch (e) {
      error = "Eroare de rețea. Verifică dacă serverul rulează.";
    }
  };

  /**
   * 3. Funcția de TOGGLE
   * Schimbă între modul 'login' și 'register'.
   */
  const toggleMode = () => {
    mode = mode === "login" ? "register" : "login";
    error = "";
    // Resetează câmpurile comune
    username = "";
    password = "";
  };
</script>
<div slass="tot">
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

  .tot{
    background-color: #93cfdf;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;


  }
  h1 {
    text-align: center;
    font-size: 2rem;
    margin: 2rem 0;
    font-family: "Momo Trust Display", sans-serif;
    color: #00246B;
  }

  .form {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 50vh;
    gap: 0.75rem;
    width: 320px;
    margin: 2rem auto;
    background: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }

  input {
    padding: 0.6rem;
    border-radius: 10px;
    border: 1px solid #ccc;
    font-size: 1rem;
  }

  button {
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
