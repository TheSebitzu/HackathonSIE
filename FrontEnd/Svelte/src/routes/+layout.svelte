<script>
  import { onMount } from 'svelte';
  import { authToken } from '$lib/authStore.js';

  // Când aplicația se încarcă în browser
  onMount(() => {
    // Sincronizăm store-ul cu ce e în localStorage
    const token = localStorage.getItem('access_token');
    authToken.set(token);
  });
</script>

<slot />