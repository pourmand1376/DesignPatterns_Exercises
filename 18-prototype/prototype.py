from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def clone(self):
        pass

class Circle(Component):
    def __init__(self):
        super().__init__()
        self.radius = None

    def render(self):
        print('Circle is rendering')

    def clone(self):
        new_circle=Circle()
        new_circle.radius = self.radius
        return new_circle
    
class ContextMenu():
    def duplicate(component: Component):
        component.clone()

