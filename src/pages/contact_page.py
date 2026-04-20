import flet as ft
from flet import (
    Page,
    Container,
    Text,
    Icons,
    alignment,
    Column,
    TextField,
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
                Text("Contact Me", size=d["heading_size"], weight=FontWeight.BOLD),
                Text(
                    "Interested in working together or just want to connect?",
                    color=ft.Colors.GREY_400,
                ),
                TextField(label="Your Name", width=d["field_width"]),
                TextField(label="Your Email", width=d["field_width"]),
                TextField(
                    label="Message",
                    multiline=True,
                    min_lines=3,
                    max_lines=5,
                    width=d["field_width"],
                ),
                ElevatedButton("Send Message", icon=Icons.SEND),
                Divider(),
                Text(
                    "Or reach out directly via the links below:",
                    size=13,
                    italic=True,
                    color=ft.Colors.GREY_400,
                ),
                ft.Row(
                    [
                        ft.TextButton(
                            "zacharylieberman1@gmail.com",
                            icon=Icons.EMAIL,
                            url="mailto:zacharylieberman1@gmail.com",
                        ),
                        ft.TextButton(
                            "LinkedIn",
                            icon=Icons.OPEN_IN_NEW,
                            url="https://www.linkedin.com/in/zachary-lieberman6",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=16,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16,
        ),
        alignment=alignment.top_center,
        expand=True,
        padding=d["padding"],
    )
