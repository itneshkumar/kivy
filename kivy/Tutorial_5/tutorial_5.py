# kvy design language use in this code
import  kivy
from kivy.app import App
from kivy.uix.button import Button
# importing the grid_layout in kivy gui
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
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
class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__=='__main__':
    MyApp().run()