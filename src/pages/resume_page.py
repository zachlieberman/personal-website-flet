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
    ElevatedButton,
    Divider,
    ListTile,
    MainAxisAlignment,
    FontWeight,
)


def get_view(page: Page) -> Container:
    return Container(
        content=Column(
            [
                # Removed the image to eliminate the gap above the title
                Text("Resume", size=32, weight=FontWeight.BOLD),
                Text("Download my full resume or view highlights below."),
                ElevatedButton(
                    "Download PDF",
                    icon=Icons.DOWNLOAD,
                    url="Zachary%20Lieberman%20Resume.pdf",
                ),
                Divider(),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=alignment.top_center,
        expand=True,
        padding=30,
    )
