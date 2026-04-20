import flet as ft
from flet import (
    Page,
    Container,
    Text,
    Icons,
    alignment,
    Column,
    Row,
    ElevatedButton,
    Divider,
    FontWeight,
)
from utils.responsive import get_dims


def _section_header(title: str, size: float) -> Text:
    return Text(title, size=size, weight=FontWeight.BOLD)


def _experience_entry(
    company: str,
    role: str,
    dates: str,
    bullets: list,
    subtext_size: float,
    width: float,
) -> Column:
    return Column(
        [
            Row(
                [
                    Text(company, weight=FontWeight.W_700, size=subtext_size),
                    Text(dates, italic=True, size=13, color=ft.Colors.GREY_400),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                width=width,
            ),
            Text(role, italic=True, size=subtext_size - 2, color=ft.Colors.BLUE_200),
            *[Text(f"• {b}", size=13) for b in bullets],
        ],
        spacing=4,
        width=width,
    )


def get_view(page: Page) -> Container:
    d = get_dims(page)
    w = d["field_width"]

    experience = Column(
        [
            _section_header("Experience", d["heading_size"]),
            _experience_entry(
                "Capital One",
                "Senior Associate Software Engineer",
                "Jan 2025 – Present",
                [
                    "Maintained Cloud Custodian Platform servicing 3,000+ AWS accounts with 200M+ daily policy executions",
                    "Built smart batch Lambdas, SQS queues, and DynamoDB logic achieving $1M+ annual cost savings",
                    "Migrated 100+ services to a new small-account model — new VPC, security groups, CloudFormation updates",
                    "Optimized report service by replacing S3 file tracking with Aurora PostgreSQL for performance and reliability",
                ],
                d["subtext_size"],
                w,
            ),
            _experience_entry(
                "Capital One",
                "Associate Software Engineer",
                "Aug 2023 – Jan 2025",
                [
                    "Designed and deployed Aurora PostgreSQL with SQLAlchemy/Alembic ORM, including networking, security, and automation",
                    "Transformed policy dry-run evaluation to full-resource impact analysis using PostgreSQL and ECS tasks",
                    "Scaled platform 300% — expanded from 2 to 6 regions for enterprise-wide compliance",
                    "Migrated time-sensitive Lambda audit report to Fargate, resolving memory and timeout constraints",
                ],
                d["subtext_size"],
                w,
            ),
        ],
        spacing=16,
        width=w,
    )

    education = Column(
        [
            _section_header("Education", d["heading_size"]),
            Column(
                [
                    Row(
                        [
                            Text(
                                "University of Virginia",
                                weight=FontWeight.W_700,
                                size=d["subtext_size"],
                            ),
                            Text("May 2023", italic=True, size=13, color=ft.Colors.GREY_400),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        width=w,
                    ),
                    Text(
                        "B.S. Computer Science · Engineering Business & Data Science Minor",
                        italic=True,
                        size=14,
                        color=ft.Colors.BLUE_200,
                    ),
                ],
                spacing=4,
                width=w,
            ),
        ],
        spacing=12,
        width=w,
    )

    other = Column(
        [
            _section_header("Certifications & Recognition", d["heading_size"]),
            Text("• AWS Certified Solutions Architect – Associate (2023)", size=13),
            Text(
                "• CapitalOne TechX 2023 Q3 Finalist — Graviton migration saving $1M+ annually",
                size=13,
            ),
            Text(
                "• Speaker: 'Defense in Depth: Guardrails in Platform Design' — Capital One SECON 2024",
                size=13,
            ),
            Text("• PyCon 2025 attendee", size=13),
            Text("• Technology Internship Program Mentor, 2024 (4 interns)", size=13),
        ],
        spacing=6,
        width=w,
    )

    return Container(
        content=Column(
            [
                Text("Resume", size=d["title_size"], weight=FontWeight.BOLD),
                ElevatedButton(
                    "Download PDF",
                    icon=Icons.DOWNLOAD,
                    url="Zachary%20Lieberman%20Resume.pdf",
                ),
                Divider(),
                experience,
                Divider(),
                education,
                Divider(),
                other,
                ft.Container(height=20),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
        ),
        alignment=alignment.top_center,
        expand=True,
        padding=d["padding"],
    )
