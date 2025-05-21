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
    TextField,
    ElevatedButton,
    Divider,
    FontWeight,
    MainAxisAlignment,
)


def get_view(page: Page) -> Container:
    return Container(
        content=Column(
            [
                Text("Contact Me", size=28, weight=FontWeight.BOLD),
                Text("I'd love to hear from you!"),
                TextField(label="Your Name", width=300),
                TextField(label="Your Email", width=300),
                TextField(
                    label="Message", multiline=True, min_lines=3, max_lines=5, width=300
                ),
                ElevatedButton("Send Message", icon=Icons.SEND),
                Divider(),
                Text("Or reach out via social links in the footer!", italic=True),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=alignment.top_center,
        expand=True,
        padding=30,
    )
