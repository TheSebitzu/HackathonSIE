<script>
  import { page } from '$app/stores';
</script>

<!-- 
  Am înlocuit wrapper-ul de swipe cu o structură
  care folosește CSS Flexbox pentru a ține
  bara de navigație în partea de jos.
-->
<div class="page-layout">
  <!-- 'main' este zona de conținut care va crește
       și va permite scroll dacă este nevoie -->
  <main>
    <!-- <slot /> va randa aici pagina ta curentă -->
    <slot />
  </main>

  <!-- Bara de navigație fixă în partea de jos -->
  <nav>
    <a 
      href="/"
      class:active={$page.url.pathname === '/'}
    >
      Acasă
    </a>
    <a 
      href="/next"
      class:active={$page.url.pathname === '/next'}
    >
      Pagina Următoare
    </a>
  </nav>
</div>

<style>
  /* Am eliminat stilurile vechi pentru .swipe-wrapper
    și am adăugat stiluri pentru noua structură.
  */
  .page-layout {
    display: flex;
    flex-direction: column;
    height: 100vh; /* Ocupă tot ecranul pe înălțime */
    width: 100vw; /* Ocupă tot ecranul pe lățime */
  }

  main {
    flex: 1; /* Permite acestei zone să crească și să umple spațiul */
    overflow-y: auto; /* Adaugă scroll DOAR la conținut, dacă e prea lung */
  }

  nav {
    flex-shrink: 0; /* Nu lasă bara de navigație să se micșoreze */
    display: flex;
    justify-content: space-around; /* Butoane distribuite egal */
    align-items: center;
    padding: 1rem;
    background-color: #f0f0f0; /* Un fundal gri deschis */
    border-top: 1px solid #ddd;
  }

  nav a {
    text-decoration: none;
    color: #333;
    font-size: 1rem;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    font-family: sans-serif;
    font-weight: bold;
    transition: background-color 0.2s;
  }

  /* Stil pentru butonul paginii active */
  nav a.active {
    background-color: #007bff;
    color: white;
  }

  /* Stiluri globale:
    Am scos 'overflow: hidden' pentru a permite scroll-ul 
    controlat de 'main'.
  */
  :global(body) {
    margin: 0;
  }

  /* Am scos stilurile globale care forțau înălțimea.
    Acum, paginile pot avea înălțimea lor naturală.
  */
  :global(.container), :global(.container-next) {
    /* Setăm 'min-height' în loc de 'height' pentru a ne asigura
      că fundalul se întinde, dar permitem și scroll
    */
    min-height: 100%;
    width: 100%;
    margin: 0;
    
    /* Atenție! Am adăugat 'box-sizing' pentru a preveni 
      probleme de layout la adăugarea de padding.
    */
    box-sizing: border-box; 
  }
</style>