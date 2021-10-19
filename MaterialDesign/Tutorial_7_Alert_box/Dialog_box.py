from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton

class MainApp(MDApp):
    dialog=None
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="BlueGray"
        return Builder.load_file('Alert.kv')
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Pretty Neat, Right?!",
                text="This is just some text goes here ..",
                buttons = [
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release= self.close_dialog
                    ),
                    MDRectangleFlatButton(
                        text="Yes It's Neat", text_color=self.theme_cls.primary_color, on_release= self.neat_dialog
                    ),


                        ],
                                )
        self.dialog.open()
    # click cancel button
    def close_dialog(self, obj):
        # close alert button
        self.dialog.dismiss()
    # click the neat button
    def neat_dialog(self, obj):
        # closer alert buttton
        self.dialog.dismiss()
        # change label button
        self.root.ids.my_label.text = "Yes It's Neat!"


MainApp().run()