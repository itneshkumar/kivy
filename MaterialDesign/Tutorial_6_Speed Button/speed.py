from kivymd.app import MDApp
from kivy.lang import Builder

class MainApp(MDApp):
    data= {
        "language-python": "Python",
        "language-ruby": "Ruby",
        "language-javascript": "JS"
    }
    def callback(self, instance):
        if instance.icon =='language-python':
            lang ='Python'
        elif instance.icon =='language-ruby':
            lang ='Ruby'
        elif instance.icon =='language-javascript':
            lang ='JS'
        self.root.ids.my_label.text=f'You pressed {lang}'
    def open(self):
        self.root.ids.my_label.text = f'open!!'
    #close
    def close(self):
        self.root.ids.my_label.text = f'close!!'

    def build(self):
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette="BlueGray"
        return Builder.load_file('speed.kv')

MainApp().run()