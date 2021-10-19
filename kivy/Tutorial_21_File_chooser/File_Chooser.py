    # we do not need to all the file in kvy just two and three file is enough
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
# set the app size
Window.size=(500,700)


Builder.load_file('File.kv')
# create the new class and inherit the Layout

class MyLayout(Widget):
    def selected(self, filename):
        try:
            self.ids.my_image.source=filename[0]
            print(filename[0])
        except:
            pass

class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__=='__main__':
    AwesomeApp().run()