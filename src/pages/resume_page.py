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
                    "Welcome to the Resume Page", size=30, color="cyan", weight="bold"
                ),
            ],
            alignment=alignment.center,
        ),
        alignment=alignment.center,
        expand=True,
    )
