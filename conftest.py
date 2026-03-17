import sys
import os
from types import ModuleType


def _noop(*_a, **_k):
    return None


class _ControlMeta(type):
    """Allows class-level attribute access for flet constants (e.g. FontWeight.BOLD, padding.symmetric(...))."""
    def __getattr__(cls, name):
        return _noop


class _Control(metaclass=_ControlMeta):
    """
    Minimal flet control stub. Stores constructor args as attributes so tests
    can traverse the component tree without importing the real flet package
    (which downloads Flutter binaries on a clean CI machine).

    - First positional list arg → stored as .controls  (Column, Row, etc.)
    - First positional str arg  → stored as .value      (Text, etc.)
    - All kwargs               → stored as attributes   (content=, alignment=, etc.)
    """
    def __init__(self, *args, **kwargs):
        if args:
            first = args[0]
            if isinstance(first, list):
                self.controls = first
            elif isinstance(first, str):
                self.value = first
        for k, v in kwargs.items():
            setattr(self, k, v)


class _FletStub(ModuleType):
    # Must be a real class so MagicMock(spec=ft.Page) works in test_main.py
    Page = _Control

    def __getattr__(self, name):
        # Handles both callable controls (Container, Text, Column, ...)
        # and constant namespaces (FontWeight, Icons, alignment, ...) via _ControlMeta.
        return _Control


# Replace flet in sys.modules before any src/ file imports it.
sys.modules["flet"] = _FletStub("flet")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
