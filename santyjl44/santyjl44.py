import reflex as rx

from .pages.home import home

from .states.logic import StateYoutube, HeroState
from .services.youtube_api import API_KEY, CHANNEL_ID
from .routers import ROUTES

app = rx.App(
    stylesheets=[
        "/keyframes.css",
        "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&display=swap",
        "https://fonts.googleapis.com/css2?family=Lora:wght@400;500;600&display=swap",
        "https://fonts.googleapis.com/css2?family=Caveat:wght@400;500;600;700&display=swap",
    ]
)
app.add_page(
    home,
    route=ROUTES["home"],
    on_load=[
        StateYoutube.load_canal_youtube(API_KEY, CHANNEL_ID ),
        HeroState.start_typewriter,
        ],
    
    )
