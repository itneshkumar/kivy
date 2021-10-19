from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('split.kv')

class MyLayout(Widget):
    pass

class AwesomeApp(App):
    def build(self):
        self.icon="Capture.png"
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
