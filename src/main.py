import flet as ft
from flet import Page
from components.footer import create_footer
from utils.routing import get_routes, update_route, route_change
from utils.tabs import get_tabs


def main(page: Page):
    page.title = "Zach's Personal Website"
    page.theme_mode = ft.ThemeMode.DARK
    page.controls.clear()

    routes = get_routes()

    # Create tabs using utility function
    tabs = get_tabs(page, lambda e: update_route(e, page, routes))

    footer = create_footer(page)
    # Add footer to the page
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

    # Register the route change handler
    page.on_route_change = lambda e: route_change(e, page, tabs, routes)

    # Initialize with the current route or default to home
    if page.route == "":
        page.route = "/home"
    # Handle initial route
    route_change(None, page, tabs, routes)


# run app
ft.app(main, assets_dir="assets")
