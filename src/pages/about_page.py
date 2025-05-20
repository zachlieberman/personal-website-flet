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
)


def get_view(page: Page) -> Container:
    return Container(
        content=Column(
            [
                Text(
                    "Welcome to the About Page", size=30, color="purple", weight="bold"
                ),
            ],
            alignment=alignment.center,
        ),
        alignment=alignment.center,
        expand=True,
    )
