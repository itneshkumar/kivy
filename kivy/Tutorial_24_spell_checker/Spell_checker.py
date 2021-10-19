    # we do not need to all the file in kvy just two and three file is enough
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.spelling import  Spelling
from kivy.core.window import Window
# set the app size
Window.size=(500,700)


Builder.load_file('spell.kv')
# create the new class and inherit the Layout

class MyLayout(Widget):
    def press(self):
        # create instance spelling
        s=Spelling()
        # select the language
        s.select_language('en_US')
        # see the language options
        print(s.list_languages())
        # grab the word from the textbox
        word=self.ids.word_input.text
        options=s.suggest(word)
        x=""
        for item in options:
            x=f'{x}\n{item}'
        # update the label
        self.ids.word_label.text=f'{x}'

class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__=='__main__':
    AwesomeApp().run()