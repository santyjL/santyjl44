from enum import Enum
import reflex as rx

class Colors(Enum):
    PRIMARY = "#ff7043"
    SECONDARY = "#ffa270"
    ACCENT = "#d81b60"
    SUCCESS = "#22c55e"
    WARNING = "#f59e0b"
    BACKGROUND = "#18150fc0"
    WHITE = "#ffffff"
    BLACK = "#000000"
    NAVBAR= "#0000"
    LINEAS= "#A3482A"
    DESTACAR = "#D68C2D"

class Font(Enum):
    TEXT_PRINCIPAL_COLOR= "#F5F2EC"

fondo = dict[str,str](
    bg="radial-gradient(circle, #550a03, #661115, transparent)",
    animation="respirar 20s linear infinite"
)

body=dict[str,str](
    bg=Colors.BACKGROUND.value,
    width="90%",
    max_width="1440px",
    border_left=f"1px solid {Colors.LINEAS.value}",
    border_right=f"1px solid {Colors.LINEAS.value}",
    margin=0
)

navbar_style = dict[str, str](
    background=Colors.NAVBAR.value,
    color=Colors.WHITE.value,
    padding="1rem",
    position="fixed",
    top="0",
    width="100%",
    z_index=10,
)

hero_style = dict[str, str](
    background_image=f"url('{rx.asset("hero.png")}')",
    background_color=Colors.BLACK.value,
    background_size="cover",
    background_position="center",
    color=Colors.WHITE.value,
    padding="4rem 2rem",
    width="100%",
    height="85vh",
    margin=0,
    border_bottom=f"1px solid {Colors.LINEAS.value}",
    text_align="right",
)

sobre_mi_style = dict[str, str](
    border_right=f"1px solid {Colors.LINEAS.value}",
    justify_items="center",
    text_align="justify",
    padding="2em",
    min_width="45%",
    flex_grow=0
)

boton_style = dict[str, str](
    background_color=Colors.DESTACAR.value,
    justify_items="center",
    padding="1.5em",
    margin="15px 0"
)

foto_sobre_mi_style = dict[str, str](
    object_fit="cover",
    min_width="50%",
    flex_grow=1,
    style=sobre_mi_style
)

sobre_mi_seccion_style = dict[str, str](
    border=f"10px solid {Colors.LINEAS.value}"
)

footer_style = dict[str, str](
    background=Colors.PRIMARY.value,
    color=Colors.WHITE.value,
    padding="2rem 1rem",
    width="100%",
    text_align="center",
)

buttons_style = dict[str, str](
    background=Colors.ACCENT.value,
    color=Colors.WHITE.value,
    padding="0.75rem 1.5rem",
    border_radius="0.5rem",
    cursor="pointer",
)


seo_style = dict[str, str]()

whatsapp_style = dict[str, str](
    background=Colors.SUCCESS.value,
    color=Colors.WHITE.value,
    padding="0.75rem",
    border_radius="50%",
    position="fixed",
    bottom="1.5rem",
    right="1.5rem",
)

youtube_style = dict[str, str](
    width= "30%",
    height="400px",
    border=f"1px solid {Colors.LINEAS.value}",
    border_top=f"6px solid {Colors.LINEAS.value}",
    border_radius="0 0 20px 20px",
    justify_items="center",
    padding="1em",
)

servicios_style = dict[str, str](
    width= "30%",
    height="400px",
    border=f"1px solid {Colors.LINEAS.value}",
    border_top=f"6px solid {Colors.LINEAS.value}",
    border_radius="0 0 20px 20px",
    justify_items="center",
    padding="1em",
)

skills_style = dict[str, str](
    width= "30%",
    height="400px",
    border=f"1px solid {Colors.LINEAS.value}",
    border_top=f"6px solid {Colors.LINEAS.value}",
    border_radius="0 0 20px 20px",
    justify_items="center",
    padding="1em"
)

spotify_style = dict[str, str](
    padding="1rem",
)

github_style = dict[str, str](
    padding="1rem",
)

weather_style = dict[str, str](
    padding="1rem",
)

proyecto_card_style = dict[str, str](
    width="100%",
    overflow="hidden",    
)

proyectos_carrusel_style = dict[str, str](
    display="flex",
    gap="0",
    width="max-content",
    border_top=f"1px solid {Colors.LINEAS.value}",
    border_bottom=f"1px solid {Colors.LINEAS.value}",
    animation="scroll_projects 20s linear infinite",
    
)

proyectos_carrusel_barra=dict[str,str](
    width="200px",
    height="250px",
    position="relative",
    z_index=20,
    border_top=f"1px solid {Colors.LINEAS.value}",
    border_bottom=f"1px solid {Colors.LINEAS.value}",
    padding="1em",
    background_color=Colors.BACKGROUND.value
)

faq_style = dict[str, str](
    padding="2rem",
    max_width="800px",
    margin="0",
)
