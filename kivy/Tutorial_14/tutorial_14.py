# we do not need to all the file in kvy just two and three file is enough
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout


Builder.load_file('update.kv')
# create the new class and inherit the Layout
class MyLayout(Widget): # you can aslo write the MyBoxLayout but not gridlayout
    def press(self):
        # create the variable for widget
        name=self.ids.name_input.text
        # print(name)
        #udate label
        self.ids.name_label.text=f'Hello {name}!'
        # clear input box
        self.ids.name_input.text=""


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__=='__main__':
    AwesomeApp().run()