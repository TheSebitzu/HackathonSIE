// Importă fișierele aplicației generate de SvelteKit
import { build, files, version } from '$service-worker';

// Un nume unic pentru cache-ul tău
const CACHE = `cache-${version}`;

// Lista tuturor fișierelor pe care le vom salva (app shell)
const ASSETS_TO_CACHE = [...build, ...files];

// 1. Evenimentul 'install' (se întâmplă o singură dată)
self.addEventListener('install', (event) => {
  // Așteaptă până când fișierele sunt adăugate în cache
  event.waitUntil(
    caches
      .open(CACHE)
      .then((cache) => cache.addAll(ASSETS_TO_CACHE))
      .then(() => self.skipWaiting())
  );
});

// 2. Evenimentul 'activate' (curăță cache-urile vechi)
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then(async (keys) => {
      // Șterge toate cache-urile care nu au versiunea curentă
      for (const key of keys) {
        if (key !== CACHE) {
          await caches.delete(key);
        }
      }
      // Spune service worker-ului să preia controlul imediat
      self.clients.claim();
    })
  );
});

// 3. Evenimentul 'fetch' (interceptează cererile)
self.addEventListener('fetch', (event) => {
  // Ignoră cererile care nu sunt GET (ex. POST către API-ul tău)
  if (event.request.method !== 'GET') {
    return;
  }

  event.respondWith(
    caches.open(CACHE).then(async (cache) => {
      // 1. Încearcă să găsești resursa în Cache
      const response = await cache.match(event.request);
      if (response) {
        return response; // O returnează din cache dacă există
      }

      // 2. Dacă nu e în cache, mergi la rețea (network)
      try {
        const networkResponse = await fetch(event.request);
        // (Opțional) Poți adăuga în cache răspunsul de la rețea aici
        // if (networkResponse.ok) {
        //   cache.put(event.request, networkResponse.clone());
        // }
        return networkResponse;
      } catch (error) {
        // Eroare de rețea (ex. ești offline)
        console.error('Fetch error:', error);
        // Aici ai putea returna o pagină "Offline" generică
      }
    })
  );
});