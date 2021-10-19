# we do not need to all the file in kvy just two and three file is enough
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('radio_button.kv')


# create the new class and inherit the Layout
class MyLayout(Widget):  # you can aslo write the MyBoxLayout but not gridlayout
    checks=[]
    def checkbox_click(self, instance, value, topping):
        if value==True:
            MyLayout.checks.append(topping) 
            tops=''
            for x in MyLayout.checks:
                tops=f'{tops} {x}'
            # self.ids.output_label.text=f'you selected: {MyLayout.checks}'
            self.ids.output_label.text=f'you selected: {tops}'
        else:
            MyLayout.checks.remove(topping)
            tops=''
            for x in MyLayout.checks:
                tops=f'{tops} {x}'
            self.ids.output_label.text=f'you selected: {tops}'


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
