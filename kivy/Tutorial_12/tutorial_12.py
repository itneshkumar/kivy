# we do not need to all the file in kvy just two and three file is enough
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.image import Image

Builder.load_file('image.kv')
# create the new class and inherit the Layout
class MyLayout(Widget): # you can aslo write the MyBoxLayout but not gridlayout
    pass


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__=='__main__':
    AwesomeApp().run()