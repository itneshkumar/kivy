# we do not need to all the file in kvy just two and three file is enough
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
# Builder.load_file('whatever.kv')
# no need to import any thing just paste all kv file in builder but more relevant than first method its so lengthy
Builder.load_string("""
<MyGridLayout>
    name: Name
    pizza: Pizza
    color: Color

    GridLayout:
        cols:1
        size: root.width, root.height
        GridLayout:
            cols:2

            Label:
                text: "Name"
            TextInput:
                id: Name
                multiline: False
            Label:
                text: "Favorite Pizza"
            TextInput:
                id: Pizza
                multiline: False
            Label:
                text: "Color"
            TextInput:
                id: Color
                multiline: False
        Button:
            text: "submit"
            font_size: 32
            on_press : root.press()
""")

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