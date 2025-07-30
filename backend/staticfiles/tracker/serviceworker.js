self.addEventListener('install', function(event) {
  console.log('[ServiceWorker] Installed');
});

self.addEventListener('activate', function(event) {
  console.log('[ServiceWorker] Activated');
});

self.addEventListener('fetch', function(event) {
  event.respondWith(fetch(event.request));
});
