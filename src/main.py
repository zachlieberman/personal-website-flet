import flet as ft
from flet import Page
from components.footer import create_footer
from utils.routing import get_routes, update_route, route_change
from utils.tabs import get_tabs


def main(page: Page):
    page.title = "Zachary Lieberman | Software Engineer"
    page.theme_mode = ft.ThemeMode.DARK

    routes = get_routes()

    def build():
        current_route = page.route or "/home"
        page.controls.clear()
        tabs = get_tabs(page, lambda e: update_route(e, page, routes))
        footer = create_footer(page)
        page.add(
            ft.Column(
                [
                    tabs,
                    footer,
                ],
                spacing=0,
                expand=True,
            )
        )
        page.on_route_change = lambda e: route_change(e, page, tabs, routes)
        page.route = current_route
        route_change(None, page, tabs, routes)

    page.on_resized = lambda e: build()
    build()


# run app
ft.app(main, assets_dir="assets")
