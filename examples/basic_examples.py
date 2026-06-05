from pyworld import ChatBot, UI, Game
from pyworld.game import GameObject

def example_chatbot():
    print("=== ChatBot Demo ===")
    chat = ChatBot(language='zh')
    
    messages = ['hello', 'thanks', 'help']
    for msg in messages:
        response = chat.talk(msg)
        print(f"User: {msg}")
        print(f"Bot: {response}\n")

def example_game():
    print("=== Game Demo ===")
    game = Game(title="Example Game", width=800, height=600)
    
    player = GameObject("Player", x=100, y=100)
    player.set_property("speed", 5)
    game.add_object(player)
    
    print(f"Game Title: {game.title}")
    print(f"Object Count: {len(game.get_objects())}")
    print(f"Player Position: ({player.x}, {player.y})")
    print(f"Player Speed: {player.get_property('speed')}\n")

def example_ui():
    print("=== UI Demo ===")
    ui = UI(title="Example UI", width=800, height=600)
    
    layout = ui.create_layout(orientation='vertical')
    label = ui.create_label("Welcome to PyWorld!", size=(200, 50))
    button = ui.create_button("Click Me", size=(100, 50))
    
    print(f"UI Title: {ui.title}")
    print(f"UI Element Count: {len(ui.get_elements())}")
    print(f"UI Size: {ui.width}x{ui.height}\n")

if __name__ == '__main__':
    example_chatbot()
    example_game()
    example_ui()