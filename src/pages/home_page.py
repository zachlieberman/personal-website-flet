import flet as ft
from flet import (
    Page,
    Container,
    Text,
    Icons,
    alignment,
    Column,
    Row,
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
                    "Hi, I'm Zachary Lieberman",
                    size=d["title_size"],
                    weight=FontWeight.BOLD,
                ),
                Text(
                    "Senior Software Engineer · AWS & Cloud Infrastructure",
                    size=d["subtext_size"],
                    color=ft.Colors.BLUE_200,
                ),
                Text(
                    "Building enterprise-scale cloud compliance platforms at Capital One.\n"
                    "AWS Certified Solutions Architect · Based in Los Angeles, CA",
                    text_align=ft.TextAlign.CENTER,
                    size=15,
                    color=ft.Colors.GREY_400,
                ),
                Row(
                    [
                        ElevatedButton(
                            "Download Resume",
                            icon=Icons.DOWNLOAD,
                            url="Zachary%20Lieberman%20Resume.pdf",
                        ),
                        ElevatedButton(
                            "GitHub",
                            icon=Icons.CODE,
                            url="https://github.com/zachlieberman",
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=16,
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
