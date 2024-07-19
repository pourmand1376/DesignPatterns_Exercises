from abc import ABC, abstractmethod
class RenderAbstract(ABC):
    @abstractmethod
    def render(self):
        pass


class ErrorDecorator(RenderAbstract):
    def __init__(self, render_abstract:RenderAbstract):
        self.render_abstract = render_abstract
    
    def render(self):
        return self.render_abstract.render() + " [Error] "
        
class MainIconDecorator(RenderAbstract):
    def __init__(self, render_abstract:RenderAbstract):
        self.render_abstract = render_abstract

    def render(self):
        return self.render_abstract.render() + " [Main] "
    
class LoadedDecorator(RenderAbstract):
    def __init__(self, render_abstract:RenderAbstract):
        self.render_abstract = render_abstract 
    
    def render(self):
        return self.render_abstract.render() + " [Loaded] "


class Artefact(RenderAbstract):
    def __init__(self, name:str):
        self.name = name

    def render(self) -> str:
        return f"{self.name}"
    

class Editor():
    def open_projects(self, path: str) -> None:
        artefacts = [MainIconDecorator(Artefact("Main")), 
                     Artefact("Demo"), 
                     LoadedDecorator(ErrorDecorator(Artefact("MailProvider"))), 
                     LoadedDecorator(Artefact("EmailClient"))]

        for artefact in artefacts:
            print(artefact.render())

editor=Editor()
editor.open_projects("...")