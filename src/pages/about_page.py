import flet as ft
from flet import (
    Page,
    Container,
    Text,
    alignment,
    Column,
    Image,
    Chip,
    FontWeight,
)
from utils.responsive import get_dims


_SKILLS = {
    "Cloud": ["AWS", "CloudFormation", "Lambda", "Fargate", "ECS", "Batch", "VPC"],
    "DevOps": ["Docker", "Kubernetes", "Terraform", "Jenkins", "Git", "n8n"],
    "Database": ["PostgreSQL", "DynamoDB", "RDS", "SQLAlchemy", "Alembic", "MySQL"],
    "Languages": ["Python", "TypeScript", "Java", "SQL", "Bash"],
}


def _skill_section(category: str, items: list) -> Column:
    return Column(
        [
            Text(category, size=13, weight=FontWeight.W_600, color=ft.Colors.BLUE_200),
            ft.Row(
                [Chip(label=ft.Text(s)) for s in items],
                wrap=True,
                spacing=6,
                run_spacing=6,
            ),
        ],
        spacing=4,
    )


def get_view(page: Page) -> Container:
    d = get_dims(page)
    skill_sections = [_skill_section(cat, items) for cat, items in _SKILLS.items()]
    return Container(
        content=Column(
            [
                Image(src="/assets/icon.png", width=d["image_sm"], height=d["image_sm"]),
                Text("About Me", size=d["heading_size"], weight=FontWeight.BOLD),
                Text(
                    "Senior Software Engineer with 2+ years at Capital One building enterprise-scale\n"
                    "cloud infrastructure. I specialize in AWS cloud compliance platforms, serverless\n"
                    "architecture, and database engineering at massive scale.",
                    text_align=ft.TextAlign.CENTER,
                    size=15,
                ),
                Text(
                    "UVA Computer Science · AWS Certified Solutions Architect · Targeting Los Angeles, CA",
                    size=13,
                    italic=True,
                    color=ft.Colors.GREY_400,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=4),
                Text("Skills", size=d["subtext_size"], weight=FontWeight.W_600),
                *skill_sections,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=d["spacing"],
            scroll=ft.ScrollMode.AUTO,
        ),
        alignment=alignment.top_center,
        expand=True,
        padding=d["padding"],
    )
