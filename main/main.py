import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class HelloText(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text="Hello", font_size=64))
class SimpleApp(App):
    def build(self):
        return HelloText()

if __name__ == "__main__":
    SimpleApp().run()