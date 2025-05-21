import flet as ft


def create_footer(page):
    linkedin_image = ft.Image(src="linkedin.png", width=24, height=24)
    github_image = ft.Image(src="github.png", width=24, height=24)
    icon_button_style = dict(
        width=40,
        height=40,
        style=ft.ButtonStyle(
            shape={"": ft.RoundedRectangleBorder(radius=8)},
            padding={"": 0},
            bgcolor={"": ft.Colors.with_opacity(0.08, ft.Colors.BLUE_GREY_900)},
        ),
    )
    return ft.Container(
        content=ft.Row(
            [
                ft.Text("2025 Zach Lieberman"),
                ft.Row(
                    [
                        ft.IconButton(
                            content=github_image,
                            tooltip="GitHub",
                            url="https://github.com/zachlieberman",
                            **icon_button_style,
                        ),
                        ft.IconButton(
                            content=linkedin_image,
                            tooltip="LinkedIn",
                            url="https://www.linkedin.com/in/zachary-lieberman6",
                            **icon_button_style,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.EMAIL,
                            tooltip="Email",
                            url="mailto:zacharylieberman1@gmail.com",
                            **icon_button_style,
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=15,
        height=60,  # Set a fixed height for the footer
    )
