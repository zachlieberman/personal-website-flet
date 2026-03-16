import flet as ft
from flet import (
    Page,
    Container,
    Text,
    Icons,
    alignment,
    Column,
    ElevatedButton,
    Divider,
    FontWeight,
)
from utils.responsive import get_dims


def get_view(page: Page) -> Container:
    d = get_dims(page)
    return Container(
        content=Column(
            [
                # Removed the image to eliminate the gap above the title
                Text("Resume", size=d["title_size"], weight=FontWeight.BOLD),
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
        padding=d["padding"],
    )
