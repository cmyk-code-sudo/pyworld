import pytest
from pyworld import ChatBot, Game, UI

def test_chatbot_init():
    chat = ChatBot(language='zh')
    assert chat.language == 'zh'

def test_chatbot_talk():
    chat = ChatBot(language='zh')
    response = chat.talk('hello')
    assert isinstance(response, str)
    assert len(response) > 0

def test_game_init():
    game = Game(title="Test Game")
    assert game.title == "Test Game"
    assert game.fps == 60

def test_ui_init():
    ui = UI(title="Test UI")
    assert ui.title == "Test UI"
    assert ui.width == 800
    assert ui.height == 600

def test_game_add_object():
    from pyworld.game import GameObject
    game = Game()
    obj = GameObject("test_obj")
    game.add_object(obj)
    assert len(game.get_objects()) == 1
    assert game.get_objects()[0].name == "test_obj"