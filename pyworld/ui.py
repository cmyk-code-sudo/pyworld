from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle

class UI:
    def __init__(self, title="PyWorld", width=800, height=600):
        self.title = title
        self.width = width
        self.height = height
        self.elements = []
        self.callbacks = {}
        self.app = None
    
    def create_label(self, text, size=(100, 50)):
        label = Label(text=text, size_hint=(None, None), size=size)
        self.elements.append(label)
        return label
    
    def create_button(self, text, callback=None, size=(100, 50)):
        button = Button(text=text, size_hint=(None, None), size=size)
        if callback:
            button.bind(on_press=callback)
            self.callbacks[text] = callback
        self.elements.append(button)
        return button
    
    def create_textinput(self, hint_text="", multiline=False, size=(300, 50)):
        textinput = TextInput(
            hint_text=hint_text,
            multiline=multiline,
            size_hint=(None, None),
            size=size
        )
        self.elements.append(textinput)
        return textinput
    
    def create_layout(self, orientation='vertical', size_hint=(1, 1)):
        if orientation == 'vertical':
            layout = BoxLayout(orientation='vertical', size_hint=size_hint)
        else:
            layout = BoxLayout(orientation='horizontal', size_hint=size_hint)
        return layout
    
    def create_grid(self, cols=1, size_hint=(1, 1)):
        grid = GridLayout(cols=cols, size_hint=size_hint)
        return grid
    
    def show_popup(self, title, content, size=(400, 300)):
        popup = Popup(title=title, content=content, size_hint=(None, None), size=size)
        popup.open()
        return popup
    
    def create_app(self, root_widget):
        class PyWorldApp(App):
            def build(self):
                self.title = self.parent_title
                return root_widget
        
        self.app = PyWorldApp()
        self.app.parent_title = self.title
        return self.app
    
    def run(self, root_widget):
        app = self.create_app(root_widget)
        app.run()
    
    def get_elements(self):
        return self.elements
    
    def clear_elements(self):
        self.elements = []