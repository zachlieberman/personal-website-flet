import pytest
from unittest.mock import MagicMock
from src.components.footer import create_footer


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


def test_footer_renders(page):
    footer = create_footer(page)
    assert hasattr(footer, "content")
    texts = get_texts_from_column(footer.content)
    assert any("Zach Lieberman" in t for t in texts)
