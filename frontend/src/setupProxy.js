const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/ws', // Proxy path
    createProxyMiddleware({
      target: 'http://backend:8000', // Backend URL
      ws: true, // Enable WebSocket proxying
      changeOrigin: true,
    })
  );
};