import pytest
from unittest.mock import MagicMock
import flet as ft
from src.pages import home_page, about_page, projects_page, resume_page, contact_page
from src.components.footer import create_footer
from src.utils.routing import get_routes, update_route, route_change
from src.utils.tabs import get_tabs


@pytest.fixture
def page():
    # Use a MagicMock to simulate the Flet Page for testing
    mock_page = MagicMock()
    mock_page.route = ""
    mock_page.update = MagicMock()
    return mock_page


def get_texts_from_column(column):
    # Helper to extract all text from a Flet Column's controls
    texts = []
    for c in getattr(column, "controls", []):
        # Flet Text control: c is ft.Text or ft.TextField
        if hasattr(c, "text") and c.text:
            texts.append(str(c.text))
        if hasattr(c, "value") and c.value:
            texts.append(str(c.value))
        if hasattr(c, "label") and c.label:
            texts.append(str(c.label))
        # Recursively check nested columns/rows/content
        if hasattr(c, "content") and hasattr(c.content, "controls"):
            texts.extend(get_texts_from_column(c.content))
        if hasattr(c, "controls"):
            texts.extend(get_texts_from_column(c))
    return texts


def test_home_page_renders(page):
    view = home_page.get_view(page)
    assert hasattr(view, "content")
    texts = get_texts_from_column(view.content)
    print("DEBUG: home_page texts:", texts)
    assert any("Welcome to my personal website!" in t for t in texts)


def test_about_page_renders(page):
    view = about_page.get_view(page)
    assert hasattr(view, "content")
    texts = get_texts_from_column(view.content)
    assert any("About Me" in t for t in texts)


def test_projects_page_renders(page):
    view = projects_page.get_view(page)
    assert hasattr(view, "content")
    texts = get_texts_from_column(view.content)
    assert any("Projects" in t for t in texts)


def test_resume_page_renders(page):
    view = resume_page.get_view(page)
    assert hasattr(view, "content")
    texts = get_texts_from_column(view.content)
    assert any("Resume" in t for t in texts)


def test_contact_page_renders(page):
    view = contact_page.get_view(page)
    assert hasattr(view, "content")
    texts = get_texts_from_column(view.content)
    assert any("Contact" in t for t in texts)


def test_footer_renders(page):
    footer = create_footer(page)
    assert hasattr(footer, "content")
    texts = get_texts_from_column(footer.content)
    assert any("Zach Lieberman" in t for t in texts)


def test_tabs_and_routing(page):
    routes = get_routes()
    tabs = get_tabs(page, lambda e: update_route(e, page, routes))
    assert tabs.selected_index == 0

    # Simulate tab change
    class E:
        control = type("obj", (), {"selected_index": 2})

    update_route(E(), page, routes)
    assert page.route == list(routes.keys())[2]
    # Simulate route change
    page.route = "/about"
    route_change(None, page, tabs, routes)
    assert tabs.selected_index == routes["/about"]
