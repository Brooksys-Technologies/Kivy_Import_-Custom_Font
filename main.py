from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.app import MDApp
#import customfont
from kivy.core.text import LabelBase # allows for importing of a custom font


#Design Our .kv design file
design= Builder.load_file('design_md_customfont.kv')

class MyLayout(Widget):
    pass

    '''
    Red,Pink, Purple, DeepPurple
    Indigo, Blue, LightBlue, Cyan
    Teal, Green, LightGreen, Lime
    Yellow, Amber, Orange, DeepOrange
    Brown, Gray, BlueGray
    Dark
    '''
class MdMainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Green"
        return MyLayout()


if __name__ == '__main__':
    #use the LabelBase to import font
    LabelBase.register(name='Neosans',fn_regular='fonts/NeoSans-Black.ttf',fn_italic='fonts/NeoSans-Black-Italic.ttf')
    # check the path above
    MdMainApp().run()
