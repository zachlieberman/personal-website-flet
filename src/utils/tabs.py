import flet as ft
from flet import Tabs, Tab, Icons, Page
from src.pages import home_page, about_page, projects_page, resume_page, contact_page
from src.components.footer import create_footer
from src.utils.routing import get_routes, update_route, route_change


def get_tabs(page: Page, on_change):
    """
    Returns a Tabs instance for the main navigation, with content for each tab.
    The on_change callback is called when the tab selection changes.
    """
    return Tabs(
        selected_index=0,
        animation_duration=300,
        on_change=on_change,
        tabs=[
            Tab(text="Home", icon=Icons.HOME, content=home_page.get_view(page)),
            Tab(text="About", icon=Icons.PERSON, content=about_page.get_view(page)),
            Tab(text="Projects", icon=Icons.WORK, content=projects_page.get_view(page)),
            Tab(
                text="Resume",
                icon=Icons.DESCRIPTION,
                content=resume_page.get_view(page),
            ),
            Tab(text="Contact", icon=Icons.EMAIL, content=contact_page.get_view(page)),
        ],
        expand=True,
        tab_alignment="center",
        padding=ft.padding.symmetric(horizontal=40),
    )
