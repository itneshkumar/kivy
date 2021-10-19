# we do not need to all the file in kvy just two and three file is enough
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('calc_addition.kv')
# create the new class and inherit the Layout

class MyLayout(Widget):
    # you can aslo write the MyBoxLayout but not gridlayout
    def clear(self):
        # create the variable for widget
        self.ids.calc_input.text="0"
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
    def add(self):
        # create the a variable that contains the boc whatever text box already
        prior = self.ids.calc_input.text
        # slap of plus sign to the test box
        self.ids.calc_input.text = f"{prior}+"
    def division(self):
        # create the a variable that contains the boc whatever text box already
        prior = self.ids.calc_input.text
        # slap of plus sign to the test box
        self.ids.calc_input.text = f"{prior}/"
    def multiply(self):
        # create the a variable that contains the boc whatever text box already
        prior = self.ids.calc_input.text
        # slap of plus sign to the test box
        self.ids.calc_input.text = f"{prior}*"
    def subtract(self):
        # create the a variable that contains the boc whatever text box already
        prior = self.ids.calc_input.text
        # slap of plus sign to the test box
        self.ids.calc_input.text = f"{prior}-"
    # create equal
    def equals(self):
        prior = self.ids.calc_input.text
        # Additon
        if "+" in prior:
            num_list = prior.split("+")
            # answer
            answer=0
            for number in num_list:
                answer=answer+int(number)
                # print the answer in the text box
            self.ids.calc_input.text=str(answer)





class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__=='__main__':
    CalculatorApp().run()