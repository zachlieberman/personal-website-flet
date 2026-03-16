import flet as ft
from flet import (
    Page,
    Container,
    Text,
    alignment,
    Column,
    Card,
    ListTile,
    FontWeight,
)
from utils.responsive import get_dims


def get_view(page: Page) -> Container:
    d = get_dims(page)
    return Container(
        content=Column(
            [
                Text("Projects", size=d["title_size"], weight=FontWeight.BOLD),
                Text("A selection of my favorite creative coding projects:"),
                Card(
                    content=ListTile(
                        leading=ft.Icon(ft.Icons.BRUSH),
                        title=ft.Text("Generative Art Gallery"),
                        subtitle=ft.Text(
                            "A collection of generative art pieces using Python and Flet."
                        ),
                        trailing=ft.IconButton(
                            icon=ft.Icons.OPEN_IN_NEW,
                            url="https://github.com/zachlieberman/generative-art",
                        ),
                    ),
                ),
                Card(
                    content=ListTile(
                        leading=ft.Icon(ft.Icons.MOVIE),
                        title=ft.Text("Interactive Visuals"),
                        subtitle=ft.Text(
                            "Live visuals for performances and installations."
                        ),
                        trailing=ft.IconButton(
                            icon=ft.Icons.OPEN_IN_NEW,
                            url="https://vimeo.com/zachlieberman",
                        ),
                    ),
                ),
                Card(
                    content=ListTile(
                        leading=ft.Icon(ft.Icons.SCHOOL),
                        title=ft.Text("Teaching & Workshops"),
                        subtitle=ft.Text(
                            "Workshops and classes on creative coding and art-tech."
                        ),
                        trailing=ft.IconButton(
                            icon=ft.Icons.OPEN_IN_NEW, url="https://sfpc.study/"
                        ),
                    ),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16,
        ),
        alignment=alignment.top_center,
        expand=True,
        padding=d["padding"],
    )
