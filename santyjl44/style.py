from enum import Enum
import reflex as rx

class Colors(Enum):
    # ==================================================
    # PALETA PRINCIPAL - CAFETERÍA
    # ==================================================

    ACCENT = "#A5502A"        # Terracota
    SUCCESS = "#22C55E"
    WARNING = "#F59E0B"
    BACKGROUND = "#F2E8D8"    # Fondo principal
    WHITE = "#F8F4EE"
    BLACK = "#000000"
    NAVBAR = "#2E1A1298"
    LINEAS = "#A5502A"
    DESTACAR = "#D38A3A"

    # ==================================================
    # COLORES ADICIONALES
    # ==================================================

    SURFACE_DARK = "#140D09"
    SURFACE_LIGHT = "#F2E8D8"

    TEXT_LIGHT = "#F8F4EE"
    TEXT_DARK = "#2A1D17"

    COFFEE_BLACK = "#140D09"
    COFFEE_DARK = "#2E1A12"
    COFFEE = "#5A3420"

    VERDE= "#56D926"

    PAPER = "#F2E8D8"
    PAPER_DARK = "#E6D8C5"


class Font(Enum):
    # Tipografías

    TITLE = "'Cormorant Garamond', serif"

    TEXT = "'Lora', serif"

    HANDWRITING = "'Caveat', cursive"

    # Colores de texto

    TEXT_PRINCIPAL_COLOR = "#F5F2EC"

    TEXT_DARK = "#2A1D17"

fondo = dict(
    bg="""
    radial-gradient(
        circle at center,
        rgba(211,138,58,0.08),
        rgba(90,52,32,0.06),
        transparent
    )
    """,
    animation="respirar 30s ease-in-out infinite"
)

body = dict(
    bg="transparent",
    color=Colors.TEXT_LIGHT.value,
    width="100%",
    max_width="1440px",
    border_left=f"1px solid {Colors.LINEAS.value}",
    border_right=f"1px solid {Colors.LINEAS.value}",
    margin="0 auto",
    font_family=Font.TEXT.value,
)

navbar_style = dict(
    background=Colors.NAVBAR.value,
    backdrop_filter="blur(12px)",
    color=Colors.WHITE.value,
    padding="1rem 2rem",
    margin="30px",
    position="fixed",
    top="0",
    border_radius="50px",
    width="80%",
    z_index=100,
)

hero_style = dict(
    background_image=f"""
    linear-gradient(
        to right,
        rgba(28,18,13,0.15),
        rgba(28,18,13,0.95)
    ),
    url('{rx.asset("hero.png")}')
    """,

    background_size="cover",
    background_position="center",
    color=Colors.WHITE.value,
    margin=0,
    width="100%",
    height="100vh",
    border_bottom=f"1px solid {Colors.LINEAS.value}",
    text_align="right",
    display="flex",
    justify_content="flex-end",
    align_items="center",
)

sobre_mi_style = dict(
    background=Colors.PAPER.value,
    color=Colors.TEXT_DARK.value,
    justify_items="center",
    text_align="justify",
    padding="4rem",
    min_width="45%",
    flex_grow=0,
    font_family=Font.TEXT.value,
)

boton_style = dict(
    background_color=Colors.DESTACAR.value,
    color=Colors.WHITE.value,
    padding="1.5rem",
    border_radius="40px",
    cursor="pointer",
    transition="all .3s ease",
    margin="15px 0",
    font_family=Font.TEXT.value,
)

foto_sobre_mi_style = dict(
    object_fit="cover",
    max_width="35%",
    margin="50px",
    border_radius="20px",
    position="relative",
    flex_grow=1,
    filter="brightness(0.85)",
)

foto_datos_style= dict(
    background_color=Colors.COFFEE.value,
    backdrop_filter="blur(12px)",
    color=Colors.TEXT_LIGHT.value,
    padding="1rem",
    display="flex",
    flex_flow="row nowrap",
    justify_content="center",
    gap="15px",
    position="absolute",
    left="67.7%",
    top="450px",
    border_radius="10px",
    height="80px",
    width="30%",
    z_index=20,
)

sobre_mi_seccion_style = dict(
    display="flex",
    flex_flow="row nowrap",
    position="relative",
    columns=2,
    margin=0,
    background=Colors.PAPER.value,
    padding="150px 0 0 0",
)

footer_style = dict(
    background=Colors.SURFACE_DARK.value,
    color=Colors.WHITE.value,
    padding="2em",
    width="100%",
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

card_trabjo = dict(
    width="30%",
    min_height="400px",
    background=Colors.PAPER.value,
    color=Colors.TEXT_DARK.value,
    border_radius=f"20px",
    padding="2rem",
    box_shadow= None,
    scale= 1,
    transition="scale 0.7s 0.3s",
    _hover={
        "scale" : "1.05",
        "box-shadow" : f"0 0 20px 0 {Colors.COFFEE.value}"
    }
)

me_diferencia_style = dict(
    overflow="hidden",
    background=Colors.PAPER_DARK.value,
    color=Colors.TEXT_DARK.value,
    gap="40px",
    justify_content="center",
    padding="150px 20px 40px 20px",
)

proyectos_style= dict(
    width="400px",
    height="250px",
    object_fit="cover",
    box_shadow=f"0 0 10px 0 {Colors.VERDE.value}",
    flex_shrink="0",
)

proyecto_card_style = dict(
    overflow="hidden",
    background=Colors.PAPER.value,
    color=Colors.TEXT_DARK.value,
    padding="150px 0 0 0"
)

proyectos_carrusel_style = dict(
    display="flex",
    gap="20px",
    width="max-content",
    padding="2rem 0",
    animation="scroll_projects 35s linear infinite",
)

proyectos_carrusel_barra = dict(
    width="260px",
    height="350px",
    position="relative",
    z_index=20,
    padding="40px",
    background_color=Colors.PAPER_DARK.value,
    
)


contacto_style= dict(
    width="100%",
    background=Colors.PAPER_DARK.value,
    padding="150px 0 150px 0 ",
)
