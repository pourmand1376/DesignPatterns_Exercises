from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def render(self):
        pass

class Circle(Component):
    def __init__(self):
        super().__init__()
        self.radius = None

    def render(self):
        print('Circle is rendering')

class ContextMenu():
    def duplicate(component: Component):
        if isinstance(component, Circle):
            radius = component.radius
            circle=Circle()
            circle.radius = radius
            return circle
        
        return ValueError("The component is not valid")


circle=Circle()
circle.radius = 9
ContextMenu().duplicate(circle)
# The problem is that ContextMenu is dependent on the circle.
# So, circle should be responsible for cloning not Context Menu. 

