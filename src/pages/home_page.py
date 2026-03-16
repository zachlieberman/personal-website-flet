import flet as ft
from flet import (
    Page,
    Container,
    Text,
    Icons,
    alignment,
    Column,
    Image,
    ElevatedButton,
    FontWeight,
    MainAxisAlignment,
)
from utils.responsive import get_dims


def get_view(page: Page) -> Container:
    d = get_dims(page)
    return Container(
        content=Column(
            [
                Image(src="/assets/icon.png", width=d["image_lg"], height=d["image_lg"]),
                Text(
                    "Welcome to my personal website!", size=d["title_size"], weight=FontWeight.BOLD
                ),
                Text("I'm Zach Lieberman, a creative coder and educator."),
                Text(
                    "Check out my latest interactive project below!",
                    size=d["subtext_size"],
                    italic=True,
                ),
                ElevatedButton(
                    "Try the Demo",
                    icon=Icons.PLAY_ARROW,
                    url="https://openprocessing.org/user/12345",
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=d["spacing"],
        ),
        alignment=alignment.top_center,
        expand=True,
        padding=d["padding"],
    )
