import pytest
from unittest.mock import MagicMock
from src.utils.routing import get_routes, update_route, route_change
from src.utils.tabs import get_tabs


@pytest.fixture
def page():
    mock_page = MagicMock()
    mock_page.route = ""
    mock_page.update = MagicMock()
    return mock_page


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
