// src/lib/authStore.js
import { writable } from 'svelte/store';
import { browser } from '$app/environment';

// --- 1. Definițiile (o singură dată) ---
const initialToken = browser ? localStorage.getItem('access_token') : null;
export const authToken = writable(initialToken);

// --- 2. Noua funcție de LOGOUT (versiunea async) ---
export async function logout() {
  const refreshToken = localStorage.getItem('refresh_token');

  if (browser) {
    try {
      // 1. Spune backend-ului să invalideze token-ul
      await fetch('http://localhost:8000/api/logout/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ refresh: refreshToken })
      });

    } catch (e) {
      console.error('Logout API call failed:', e);
    }

    // 2. Curăță local storage
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    authToken.set(null);
    
    // 3. Redirecționează spre pagina de login
    window.location.href = '/auth';
  }
}

// --- 3. Sincronizarea cu localStorage (pe care o aveai la final) ---
authToken.subscribe(value => {
  if (browser) {
    if (value) {
      localStorage.setItem('access_token', value);
    } else {
      localStorage.removeItem('access_token');
    }
  }
});