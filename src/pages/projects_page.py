import flet as ft
from flet import (
    Page,
    Container,
    Text,
    alignment,
    Column,
    Card,
    ListTile,
    FontWeight,
)
from utils.responsive import get_dims


_PROJECTS = [
    {
        "icon": ft.Icons.CLOUD,
        "title": "AI Workflow Platform",
        "date": "Apr – May 2025",
        "subtitle": (
            "Self-hosted n8n automation platform on AWS EC2 with Docker Compose orchestration. "
            "Designed for AI-powered workflow automation via custom HTTP nodes and external API integrations."
        ),
        "url": "https://github.com/zachlieberman",
        "tags": ["AWS EC2", "Docker", "n8n", "DevOps"],
    },
    {
        "icon": ft.Icons.SMART_TOY,
        "title": "Team Slack Bot",
        "date": "Dec 2024 – Jan 2025",
        "subtitle": (
            "Bolt Python Slack bot hosted on AWS Fargate integrating PagerDuty and ServiceNow APIs "
            "for recurring team information — built during a 2-week innovation sprint."
        ),
        "url": None,
        "tags": ["Python", "AWS Fargate", "Slack", "CloudFormation"],
    },
    {
        "icon": ft.Icons.WEB,
        "title": "Personal Portfolio Website",
        "date": "2025",
        "subtitle": (
            "This site — built with Python and Flet (Flutter-backed). "
            "Responsive design, automated tests with pytest, CI/CD via GitHub Actions, and pre-commit hooks."
        ),
        "url": "https://github.com/zachlieberman",
        "tags": ["Python", "Flet", "pytest", "GitHub Actions"],
    },
]


def _project_card(project: dict) -> Card:
    tag_row = ft.Row(
        [
            ft.Container(
                content=ft.Text(tag, size=11, color=ft.Colors.BLUE_200),
                padding=ft.padding.symmetric(horizontal=8, vertical=3),
                border_radius=12,
                bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.BLUE_GREY_900),
            )
            for tag in project["tags"]
        ],
        wrap=True,
        spacing=6,
        run_spacing=4,
    )
    trailing = (
        ft.IconButton(icon=ft.Icons.OPEN_IN_NEW, url=project["url"])
        if project["url"]
        else None
    )
    return Card(
        content=ft.Container(
            content=Column(
                [
                    ListTile(
                        leading=ft.Icon(project["icon"]),
                        title=ft.Text(project["title"], weight=FontWeight.W_600),
                        subtitle=ft.Text(
                            project["date"],
                            size=12,
                            italic=True,
                            color=ft.Colors.GREY_400,
                        ),
                        trailing=trailing,
                    ),
                    ft.Container(
                        content=Column(
                            [
                                ft.Text(project["subtitle"], size=13),
                                tag_row,
                            ],
                            spacing=8,
                        ),
                        padding=ft.padding.only(left=16, right=16, bottom=12),
                    ),
                ],
                spacing=0,
            ),
        ),
    )


def get_view(page: Page) -> Container:
    d = get_dims(page)
    return Container(
        content=Column(
            [
                Text("Projects", size=d["title_size"], weight=FontWeight.BOLD),
                Text(
                    "A selection of projects I've built outside of work:",
                    color=ft.Colors.GREY_400,
                ),
                *[_project_card(p) for p in _PROJECTS],
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16,
            scroll=ft.ScrollMode.AUTO,
        ),
        alignment=alignment.top_center,
        expand=True,
        padding=d["padding"],
    )
