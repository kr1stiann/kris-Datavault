import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Proxy API requests to Flask backend
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/items': {
        target: 'http://localhost:5001',
        changeOrigin: true,
      },
    },
  },
})
