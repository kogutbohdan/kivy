from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.codeinput import CodeInput
from pygments.lexers import CythonLexer

class WidgetsGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(cols=2,**kwargs)
        self.__elements=[]

    def add_widget(self, widget, *args, **kwargs):
        self.__elements.append(widget)
        super().add_widget(widget, *args, **kwargs)

    def read(self,callback):
        for widget in self.__elements:
            callback(widget)

class WidgetsOne(WidgetsGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Class One',opacity=0))
        self.add_widget(TextInput(multiline=False,opacity=0))
        self.add_widget(Button(text='Button 1',opacity=0))
        self.add_widget(Spinner(text='Home',values=('Home', 'Work', 'Other', 'Custom'),opacity=0))



class WidgetsTwo(WidgetsGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Class Two',opacity=0))
        self.add_widget(TextInput(multiline=False,opacity=0))
        self.add_widget(TextInput(multiline=False,opacity=0))
        self.add_widget(CodeInput(lexer=CythonLexer(),opacity=0))

class WidgetsThree(WidgetsGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Class Three',opacity=0))
        self.add_widget(Button(text='Button 2',opacity=0))
        self.add_widget(Button(text='Button 3',opacity=0))

class WidgetsFour(WidgetsGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Class Four',opacity=0))
        self.add_widget(Button(text='Button 4',opacity=0))
        self.add_widget(TextInput(multiline=False,opacity=0))
