"""
    Miles to Km converter.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class DistanceConverter(App):
    """ Converts Miles to KM """
    def build(self):
        self.title = 'Convert Miles to Km'
        self.root = Builder.load_file('milesToKm.kv')
        Window.size = (400, 200)
        return self.root

    def change_text(self,value):
        new_number = self.check_input() + value
        self.root.ids.input_number.text = str(new_number)

    def handle_calc(self):
        result = 1.60934 * self.check_input()
        self.root.ids.output_label.text = str(result)

    def check_input(self):
        try:
            number = float(self.root.ids.input_number.text)
        except ValueError:
            number = 0
        return number


DistanceConverter().run()
