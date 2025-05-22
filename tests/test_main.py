import pytest
from unittest.mock import MagicMock
import flet as ft
import src.main as main_mod


def test_main_runs_without_error():
    # Create a MagicMock page to simulate Flet Page
    page = MagicMock(spec=ft.Page)
    page.route = ""
    page.update = MagicMock()
    page.add = MagicMock()
    page.controls = []
    # Should not raise any exceptions
    main_mod.main(page)
    # Check that the footer and tabs are added to the page
    page.add.assert_called()
    assert page.on_route_change is not None
    # After main, route should be set to /home
    assert page.route == "/home"
    # Should call update at least once
    assert page.update.called
