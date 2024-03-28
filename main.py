from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from Window import GlobalWindow

class MyApp(App):
    def build(self):
        windowController = ScreenManager()
        windowController.add_widget(GlobalWindow(windowController=windowController))
        return windowController


if __name__ == '__main__':
    MyApp().run()