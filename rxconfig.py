import reflex as rx

config = rx.Config(
    app_name="santyjl44",
    show_built_with_reflex=False,
    api_url="https://santyjl44-production.up.railway.app",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)