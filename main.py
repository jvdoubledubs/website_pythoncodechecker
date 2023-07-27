import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


Config.set('graphics', 'resizable', True)
class PythoncodeCheck(App):

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        #Run Button
        rl = RelativeLayout(size=(300, 300))
        b1 = Button(text="Check Code", size_hint =(.3, .1), pos_hint = {"x":.35,"y":.9}, background_color = "green")
        rl.add_widget(b1)


        # Text Box for code
        b = BoxLayout(orientation='vertical')
        Color = (0,0,0,0)
        border_width = 5
        l = Label(text="                        Paste Code here!", font_size=36, color="black", y = 800)
        t = TextInput(font_size=24, size_hint_y=None,pos_hint = {"x":.01,"y":.1},size_hint = (.5,.7))
        f = FloatLayout()
        s = Scatter()
        f.add_widget(s)
        s.add_widget(l)

        rl.add_widget(t)
        rl.add_widget(f)

        return rl

if __name__ == "__main__":
    PythoncodeCheck().run()

