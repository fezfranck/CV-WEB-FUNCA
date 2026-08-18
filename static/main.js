// main.js - Comportamiento global del sitio web (Francisco Esparza)

document.addEventListener('DOMContentLoaded', () => {
    // 1. CONTROL DE LA BARRA DE NAVEGACIÓN STICKY
    const navbar = document.querySelector('.navbar-header');
    
    if (navbar) {
        const checkScroll = () => {
            if (window.scrollY > 20) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        };
        
        // Ejecutar al inicio y en cada scroll
        checkScroll();
        window.addEventListener('scroll', checkScroll);
    }

    // 2. MENÚ RESPONSIVE MÓVIL
    const toggleBtn = document.getElementById('navbar-toggle-btn');
    const navMenu = document.getElementById('navbar-menu');
    
    if (toggleBtn && navMenu) {
        // Abrir/cerrar menú al hacer clic en el botón
        toggleBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            toggleBtn.classList.toggle('active');
            navMenu.classList.toggle('active');
            document.body.classList.toggle('menu-open');
        });

        // Cerrar menú al hacer clic en cualquier enlace
        const navLinks = navMenu.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                toggleBtn.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.classList.remove('menu-open');
            });
        });

        // Cerrar menú al hacer clic fuera del mismo
        document.addEventListener('click', (e) => {
            if (navMenu.classList.contains('active') && 
                !navMenu.contains(e.target) && 
                !toggleBtn.contains(e.target)) {
                toggleBtn.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.classList.remove('menu-open');
            }
        });
    }

    // 3. OBSERVADOR DE INTERSECCIÓN (Intersection Observer) PARA ANIMACIONES
    const revealElements = document.querySelectorAll('.reveal');
    
    if ('IntersectionObserver' in window && revealElements.length > 0) {
        const revealCallback = (entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Agregar clase visible para activar animación CSS
                    entry.target.classList.add('visible');
                    // Una vez revelado, dejamos de observarlo para optimizar rendimiento
                    observer.unobserve(entry.target);
                }
            });
        };

        const revealObserver = new IntersectionObserver(revealCallback, {
            root: null, // viewport
            threshold: 0.1, // trigger cuando el 10% es visible
            rootMargin: '0px 0px -50px 0px' // se activa un poco antes de que entre
        });

        revealElements.forEach(el => {
            revealObserver.observe(el);
        });
    } else {
        // Fallback para navegadores antiguos: hacer visibles todos los elementos inmediatamente
        revealElements.forEach(el => {
            el.classList.add('visible');
        });
    }
});
