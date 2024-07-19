
class Artefact:
    def __init__(self, name:str, has_error:bool=False, is_main:bool=False, loaded:bool=False):
        self.name = name
        self.has_error = has_error
        self.is_main = is_main
        self.loaded = loaded

    def render(self) -> str:
        """
        // The current implementation is not easily extensible. If tomorrow we need
        // to support other special markers, we have to come back and modify this class.
        //
        // For example, if the project is under source control, we need to highlight
        // the artefacts that are changed but not committed to the repository with a
        // special marker.
        //
        // Similarly, if an artefact is excluded from the project, we may want to
        // make the icon look disabled or semi-transparent.
        //
        // Every time we need to support a new marker, we have to come back and modify
        // this class. Over time, the code in this class gets more and more convoluted
        // with several if statements and additional fields.
        """
        error_icon =  " [Error] " if self.has_error else ""
        main_icon = " [Main] " if self.is_main else ""
        
        other_logic = " [Loaded] " if self.loaded else ""
        return f"{self.name}{error_icon}{main_icon}{other_logic}"
    
# refactor this code so that adding a new logic is easier and more extensible. 
# Take note that IF we are not always appending something to the string.
# we append something to the string if a certain logic is True
# we may not want to apply every logic to every item! 
# Name is always visible

class Editor():
    def open_projects(self, path: str) -> None:
        artefacts = [Artefact("Main"), 
                     Artefact("Demo"), 
                     Artefact("MailProvider"), 
                     Artefact("EmailClient")]
        
        artefacts[0].is_main = True
        artefacts[2].has_error = True
        artefacts[3].loaded = True

        for artefact in artefacts:
            print(artefact.render())

editor=Editor()
editor.open_projects("...")