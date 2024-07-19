from documentState import DocumentState
class Document():
    def __init__(self, content: str = '',
                 fontName: str = '',
                 fontSize: int = 0):
        self.content = content
        self.fontName = fontName
        self.fontSize = fontSize

    def __str__(self):
        return f"Content: {self.content}, FontName: {self.fontName}, FontSize: {self.fontSize}"

    def showDocument(self):
        pass

    def create_state(self):
        return DocumentState(self.content, self.fontName, self.fontSize)

    def restore_state(self,state:DocumentState):
        self.content = state.content
        self.fontName = state.fontName
        self.fontSize = state.fontSize
    