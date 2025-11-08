// src/routes/(app)/+layout.js

import { browser } from '$app/environment';
import { redirect } from '@sveltejs/kit';

export function load() {
  // Verificăm DOAR în browser, deoarece localStorage nu există pe server
  if (browser) {
    const token = localStorage.getItem('access_token');

    // Dacă NU există token
    if (!token) {
      // Trimite utilizatorul la pagina de login.
      // 307 este un "Temporary Redirect"
      throw redirect(307, '/auth');
    }
  }

}

