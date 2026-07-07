import reflex as rx

proyectos = [
    {
        "src": rx.asset("proyectos/proyecto1.png"),
        "titulo": "MyStats De Spotify",
        "descripcion": "Una forma diferente de explorar tu música. Esta aplicación transforma los datos de Spotify en estadísticas visuales para descubrir tus artistas más escuchados, canciones favoritas y hábitos de escucha a lo largo del tiempo.",
        "url":"https://mi-stats-spotify.vercel.app/"
    },
    {
        "src": rx.asset("proyectos/proyecto2.png"),
        "titulo": "Juegos Matematicos",
        "descripcion": "Aprender matemáticas no tiene por qué sentirse como una obligación. Esta plataforma convierte conceptos como ecuaciones y sucesiones en desafíos interactivos que fomentan la práctica y el aprendizaje mediante el juego.",
        "url":"https://juegos-matematicos-tawny.vercel.app/"
    },
    {
        "src": rx.asset("proyectos/proyecto3.png"),
        "titulo": "Tarjeta De Boda",
        "descripcion": "Una experiencia digital diseñada para acompañar un momento especial. Los invitados pueden acceder a fotografías, recuerdos e información del evento desde cualquier dispositivo, conservando la esencia de la celebración en un solo lugar.",
        "url":"https://raul-y-tatiana.vercel.app/"
    },
    {
        "src": rx.asset("proyectos/proyecto3.png"),
        "titulo": "Tarjeta De Boda",
        "descripcion": "Una experiencia digital diseñada para acompañar un momento especial. Los invitados pueden acceder a fotografías, recuerdos e información del evento desde cualquier dispositivo, conservando la esencia de la celebración en un solo lugar.",
        "url":"https://raul-y-tatiana.vercel.app/"
    },
]

caracteristicas_plan_basico: list[str] = [
    "Diseño personalizado",
    "Diseño adaptable a móviles",
    "Formulario de contacto",
    "Integración de redes sociales",
    "Optimización básica de velocidad",
    "Despliegue gratuito en Vercel",
    "Entrega en 3 a 5 días",
]

caracteristicas_plan_profesional: list[str] = [
    "Todo lo incluido en el Plan Básico",
    "Galería de imágenes",
    "Animaciones",
    "Google Maps integrado",
    "SEO básico",
    "Optimización de velocidad",
    "Soporte durante 15 días",
    "Entrega en 5 a 7 días",
]

caracteristicas_plan_premium: list[str] = [
    "Todo lo incluido en el Plan Profesional",
    "Integración de APIs públicas",
    "Estadísticas y métricas",
    "Blog o catálogo informativo",
    "Panel de contenido autogestionable",
    "Optimización SEO avanzada",
    "Diseño completamente a medida",
    "Soporte prioritario durante 30 días",
    "Entrega de 5 a 9 días"
]