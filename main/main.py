import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class HelloText(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Hello", font_size=64))
        
        #button to move screens
        mainPageButton = Button(text = "Mow")
        mainPageButton.bind(on_press=self.ChangeScreens)
        layout.add_widget(mainPageButton)
        
        self.add_widget(layout)
        
    def ChangeScreens(self, *args):
        self.manager.current = "Mow_screen"
        
class mow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="mow", font_size=64))
        
        returnToMainButtton = Button(text="retorn")
        returnToMainButtton.bind(on_press=self.ChangeScreens)
        layout.add_widget(returnToMainButtton)
        
        self.add_widget(layout)
        
    def ChangeScreens(self, *args):
        self.manager.current = "main_screen"
        
class SimpleApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HelloText(name="main_screen"))
        sm.add_widget(mow(name="Mow_screen"))
        return sm

if __name__ == "__main__":
    SimpleApp().run()