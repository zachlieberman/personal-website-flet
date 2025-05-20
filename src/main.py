import flet as ft
from flet import View, Tabs, Tab, Icons
from pages import (
    home_page,
    page_not_found_error,
    about_page,
    contact_page,
    projects_page,
    resume_page,
)


def main(page: ft.Page):
    page.title = "Zach's Personal Website"

    tabs = Tabs(
        selected_index=0,
        animation_duration=300,
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
            Tab(
                text="Error",
                icon=Icons.ERROR,
                content=page_not_found_error.get_view(page),
            ),
        ],
        expand=True,
        tab_alignment="center",
        padding=ft.padding.symmetric(horizontal=40),
    )

    page.add(tabs)


ft.app(main)
