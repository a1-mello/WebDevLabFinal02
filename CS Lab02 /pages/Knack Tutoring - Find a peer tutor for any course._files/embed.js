((url, id) => {
  if (document.getElementById(id)) return;
  const script = document.createElement('script');
  script.src = url;
  script.id = id;
  script.type = 'module';
  script.crossOrigin = 'anonymous';
  document.body.appendChild(script);
})('https://embed.released.so/Dtt8OHVr/index-Dtt8OHVr.js', 'released-embed-script');

((origins) => {
  origins.forEach((origin, index) => {
    const id = `released-preconnect-${index}`;
    if (document.getElementById(id)) return;
    const link = document.createElement('link');
    link.rel = 'preconnect';
    link.href = origin;
    link.id = id;
    document.head.appendChild(link);
  });
})(['https://api.released.so', 'https://secure.released.so']);
