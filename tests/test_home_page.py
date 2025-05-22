import pytest
from unittest.mock import MagicMock
from src.pages import home_page


def get_texts_from_column(column):
    texts = []
    for c in getattr(column, "controls", []):
        if hasattr(c, "text") and c.text:
            texts.append(str(c.text))
        if hasattr(c, "value") and c.value:
            texts.append(str(c.value))
        if hasattr(c, "label") and c.label:
            texts.append(str(c.label))
        if hasattr(c, "content") and hasattr(c.content, "controls"):
            texts.extend(get_texts_from_column(c.content))
        if hasattr(c, "controls"):
            texts.extend(get_texts_from_column(c))
    return texts


@pytest.fixture
def page():
    mock_page = MagicMock()
    mock_page.route = ""
    mock_page.update = MagicMock()
    return mock_page


def test_home_page_renders(page):
    view = home_page.get_view(page)
    assert hasattr(view, "content")
    texts = get_texts_from_column(view.content)
    assert any("Welcome to my personal website!" in t for t in texts)
