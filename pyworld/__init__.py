try:
    from . import _pyworld_core
except ImportError:
    _pyworld_core = None

from .chat import ChatBot
from .ui import UI
from .game import Game

__version__ = "0.1.0"
__author__ = "cmyk-code-sudo"

__all__ = [
    'ChatBot',
    'UI',
    'Game',
    'get_core_module',
]

def get_core_module():
    return _pyworld_core