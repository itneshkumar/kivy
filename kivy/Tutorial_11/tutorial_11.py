# we do not need to all the file in kvy just two and three file is enough
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('Tutorial_11.kv')
# create the new class and inherit the Layout
class MyLayout(Widget): # you can aslo write the MyBoxLayout but not gridlayout
    pass


class AwesomeApp(App):
    def build(self):
        Window.clearcolor =(1,0,0,1)
        return MyLayout()


if __name__=='__main__':
    AwesomeApp().run()