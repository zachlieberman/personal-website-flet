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
                Text("I'd love to hear from you!"),
                TextField(label="Your Name", width=d["field_width"]),
                TextField(label="Your Email", width=d["field_width"]),
                TextField(
                    label="Message", multiline=True, min_lines=3, max_lines=5, width=d["field_width"]
                ),
                ElevatedButton("Send Message", icon=Icons.SEND),
                Divider(),
                Text("Or reach out via social links in the footer!", italic=True),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=alignment.top_center,
        expand=True,
        padding=d["padding"],
    )
