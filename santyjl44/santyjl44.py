import reflex as rx

from .pages.home import home
from .pages.about import about
from .pages.services import services
from .pages.contact import contact
from .states.logic import StateYoutube
from .services.youtube_api import API_KEY, CHANNEL_ID
from .routers import ROUTES

app = rx.App(
    stylesheets=[
        "/keyframes.css"
    ]
)
app.add_page(home, route=ROUTES["home"], on_load=StateYoutube.load_canal_youtube(API_KEY, CHANNEL_ID))
app.add_page(about, route=ROUTES["about"])
app.add_page(services, route=ROUTES["services"])
app.add_page(contact, route=ROUTES["contact"])
