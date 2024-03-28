def startWindow(current,type,windowController,children=None):
    w = type(windowController,children) if(children) else type(windowController)
    windowController.remove_widget(current)
    windowController.add_widget(w)