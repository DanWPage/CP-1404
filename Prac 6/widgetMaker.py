"""
Widget Maker
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class WidgetMaker(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names_list = ['Monkey', 'Pigsy', 'Sandy', 'TrippyTaco']

    def build(self):
        self.title = 'Widget Maker'
        self.root = Builder.load_file('widgetMaker.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names_list:
            new_button = Button(text=name)
            self.root.ids.big_box.add_widget(new_button)

WidgetMaker().run()
