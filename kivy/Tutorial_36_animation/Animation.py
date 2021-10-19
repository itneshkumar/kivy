from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation

Builder.load_file('animation.kv')

class MyLayout(Widget):
    def animate_it(self, widget, *args):
        # define the animation, you want to do
        animate = Animation(
            background_color=(0,0,1,1),
            duration=1)
            #opacity=0 )
        # do second animation
        animate += Animation(
            size_hint=(1,1))
            #opacity=0, duration=5)
        # do third animation
        animate += Animation(
            size_hint=(.5,.5))
        animate += Animation(
            pos_hint = {"center_x": 0.1})
        animate += Animation(
            pos_hint =  {"center_x": 0.5})
        # start the animation
        animate.start(widget)

        # create the callback
        animate.bind(on_complete=self.my_callback)
    def my_callback(self, *args):
        self.ids.my_label.text = "wow! Look at That!"

class AwesomeApp(App):
    def build(self):
        return MyLayout()
if __name__=="__main__":
    AwesomeApp().run()