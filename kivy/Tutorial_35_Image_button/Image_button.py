from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('button.kv')

class MyLayout(Widget):
    def hello_on(self):
        # self.ids.my_label.text="you press the button!"
        self.ids.my_image.source= "login_press.png"

    def hello_off(self):
        self.ids.my_image.source = "login1.png"
        self.ids.my_label.text = "you press the button!"


class Awesomeapp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    Awesomeapp().run()