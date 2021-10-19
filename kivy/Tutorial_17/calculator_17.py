# we do not need to all the file in kvy just two and three file is enough
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
# set the app size
Window.size=(500,700)


Builder.load_file('calc.kv')
# create the new class and inherit the Layout

class MyLayout(Widget):
    # you can aslo write the MyBoxLayout but not gridlayout
    def clear(self):
        # create the variable for widget
        self.ids.calc_input.text="0"
    # create the function to remove the last charector of the function
    def remove(self):
        prior = self.ids.calc_input.text
        # remove the last item of the text box
        prior = prior[:-1]
        self.ids.calc_input.text = prior
    # create the function makes number positive and negative
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # test to see the if - sign already
        if "-" in prior:
            self.ids.calc_input.text=f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text=f'-{prior}'

    def button_press(self, button):
        # create the a variable that contains the boc whatever text box already
        prior = self. ids.calc_input.text
        # determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
    # create the addition function
    def math_sign(self, sign):
        # create the a variable that contains the boc whatever text box already
        prior = self.ids.calc_input.text
        # slap of plus sign to the test box
        self.ids.calc_input.text = f"{prior}{sign}"
    # create the decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        # if dot then don't add dot
        if "." in prior:
            pass
        else:
            # add decimal to the end of the text
            prior=f'{prior}.'
            # output back to the text box
            self.ids.calc_input.text = prior

    def equals(self):
        prior = self.ids.calc_input.text
        # Additon
        if "+" in prior:
            num_list = prior.split("+")
            # answer
            answer= 0.0
            for number in num_list:
                answer=answer+float(number)
                # print the answer in the text box
            self.ids.calc_input.text=str(answer)





class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__=='__main__':
    CalculatorApp().run()