function revealCatalog() {
    const splash = document.getElementById('heroSplash');
    const catalog = document.getElementById('museumCatalog');

    if (splash && catalog) {
        // Ejecuta la animación de salida de la pantalla de bienvenida
        splash.classList.add('splash-hidden');
        
        // Muestra el catálogo con fundido suave
        catalog.classList.add('catalog-visible');

        // Elimina el splash del DOM tras terminar la animación
        setTimeout(() => {
            splash.style.display = 'none';
        }, 900);
    }
}