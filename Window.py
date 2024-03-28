from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from animation import animation,animation2,startAnimation
from startWindow import startWindow
from Widgets import*

class GlobalWindow(Screen):
    def startWindowF(self,windowController):
        return lambda children=None:lambda e:startWindow(self,Window,windowController,children)

    def __init__(self,windowController,**kwargs):
        super().__init__(**kwargs)
        self.__start=self.startWindowF(windowController)
        self.__btns=[
            [Button(text="open 1 window"),self.__start(WidgetsOne())],
            [Button(text="open 2 window"),self.__start(WidgetsTwo())],
            [Button(text="open 3 window"),self.__start(WidgetsThree())],
            [Button(text="open 4 window"),self.__start(WidgetsFour())]
        ]
        self.__init()

    def __init(self):
        conteiner=BoxLayout(orientation="vertical",padding=(20,20,20,20))
        i=0
        for btn in self.__btns:
            btn[0].size_hint_x=0
            btn[0].opacity=0
            btn[0].bind(on_press=btn[1])
            Clock.schedule_once(startAnimation(animation,btn[0]),i)
            i+=0.4
            conteiner.add_widget(btn[0])
        self.add_widget(conteiner)

class Window(Screen):
    def returnF(self,windowController):
        return lambda e:startWindow(self, GlobalWindow, windowController)

    def __init__(self,windowController,children=None,**kwargs):
        super().__init__(**kwargs)
        self.__init(windowController,children)

    def __init(self,windowController,children):
        box=BoxLayout(orientation="vertical",padding=(10,100,10,100))
        if children:
            box.add_widget(children)
        btn=Button(text="return",opacity=0,size_hint_y=0)
        btn.bind(on_press=self.returnF(windowController=windowController))
        animation2.start(btn)
        children.read(lambda widget:Clock.schedule_once(startAnimation(animation2,widget),0.5))

        box.add_widget(btn)
        self.add_widget(box)