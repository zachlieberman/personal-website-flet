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
    ElevatedButton,
    FontWeight,
    MainAxisAlignment,
)


def get_view(page: Page) -> Container:
    return Container(
        content=Column(
            [
                Image(src="/assets/icon.png", width=120, height=120),
                Text(
                    "Welcome to my personal website!", size=32, weight=FontWeight.BOLD
                ),
                Text("I'm Zach Lieberman, a creative coder and educator."),
                Text(
                    "Check out my latest interactive project below!",
                    size=18,
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
            spacing=20,
        ),
        alignment=alignment.top_center,
        expand=True,
        padding=30,
    )
