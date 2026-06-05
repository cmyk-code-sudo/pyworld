def main():
    from .chat import ChatBot
    from .ui import UI
    from .game import Game
    
    print("Welcome to PyWorld!")
    print("=" * 40)
    
    chat = ChatBot(language='zh')
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
        
        response = chat.talk(user_input)
        print(f"Bot: {response}")

if __name__ == '__main__':
    main()