from dataclasses import dataclass

class Observer():
    def __init__(self):
        self.observer = []

    def attach(self, observer):
        self.observer.append(observer)

    def notify_observers(self):
        for observer in self.observer:
            observer()

class UIControl(Observer):
    pass

class Button(UIControl):
    def __init__(self):
        super(Button, self).__init__()
        self._enabled = False
    @property
    def enabled(self):
        return self._enabled
    
    @enabled.setter
    def enabled(self,value):
        self._enabled = value
        self.notify_observers()


class CheckBox(UIControl):
    def __init__(self):
        super(CheckBox, self).__init__()
        self._checked = False

    @property
    def checked(self):
        return self._checked
    
    @checked.setter
    def checked(self, value):
        self._checked = value
        self.notify_observers()


class TextBox(UIControl):
    def __init__(self):
        super(TextBox, self).__init__()
        self._content = ''
        
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value):
        self._content = value
        self.notify_observers()




