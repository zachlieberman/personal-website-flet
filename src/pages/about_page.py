import flet as ft
from flet import (
    Page,
    Container,
    Row,
    Text,
    alignment,
    Column,
    Image,
    Chip,
    FontWeight,
)
from utils.responsive import get_dims


def get_view(page: Page) -> Container:
    d = get_dims(page)
    return Container(
        content=Column(
            [
                Image(src="/assets/icon.png", width=d["image_sm"], height=d["image_sm"]),
                Text("About Me", size=d["heading_size"], weight=FontWeight.BOLD),
                Text(
                    "I'm a creative technologist passionate about art, code, and education."
                ),
                Text(
                    "Fun Fact: I co-founded the School for Poetic Computation!",
                    size=16,
                    italic=True,
                ),
                Text("Skills:", size=d["subtext_size"], weight=FontWeight.W_600),
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
        padding=d["padding"],
    )
