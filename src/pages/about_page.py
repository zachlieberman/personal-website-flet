import flet as ft
from flet import (
    Page,
    Container,
    Row,
    Text,
    FloatingActionButton,
    Icons,
    SafeArea,
    alignment,
    Column,
    Image,
    Chip,
    MainAxisAlignment,
    FontWeight,
)


def get_view(page: Page) -> Container:
    return Container(
        content=Column(
            [
                Image(src="/assets/icon.png", width=80, height=80),
                Text("About Me", size=28, weight=FontWeight.BOLD),
                Text(
                    "I'm a creative technologist passionate about art, code, and education."
                ),
                Text(
                    "Fun Fact: I co-founded the School for Poetic Computation!",
                    size=16,
                    italic=True,
                ),
                Text("Skills:", size=18, weight=FontWeight.W_600),
                Row(
                    [
                        Chip(label=ft.Text("Python")),
                        Chip(label=ft.Text("Flet")),
                        Chip(label=ft.Text("Creative Coding")),
                        Chip(label=ft.Text("Teaching")),
                    ],
                    spacing=8,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=alignment.top_center,
        expand=True,
        padding=30,
    )
