# we do not need to all the file in kvy just two and three file is enough
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
Builder.load_file('whatever.kv')
# create the new class and inherit the Layout
class MyGridLayout(Widget):
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)


            # CLEAR the input boxes
    def press(self):
        Name = self.name.text
        Pizza = self.pizza.text
        Color = self.color.text

        print(f'Hello{Name}, You like {Pizza} pizza and favorait color{Color}')
        # import kivy design app file

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class AwesomeApp(App):
    def build(self):
        return MyGridLayout()

if __name__=='__main__':
    AwesomeApp().run()