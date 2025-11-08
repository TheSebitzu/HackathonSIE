import tailwindcss from '@tailwindcss/vite';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [tailwindcss(), sveltekit()],
	server: {
    host: '0.0.0.0', // <-- !! ADD THIS !! Make Svelte listen on all IPs
    proxy: {
      // All requests starting with /api will be proxied
      '/api': {
        target: 'http://127.0.0.1:8000', // <-- Your Django server
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''), // Removes /api from the request
      }
    }
  }
});
