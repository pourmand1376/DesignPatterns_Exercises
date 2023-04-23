class VideoEditor:
    def __init__(self):
        self._contrast = 0.5
        self.text = ""

    def set_text(self, text):
        self.text = text
    
    def remove_text(self):
        self.text = ""

    @property
    def contrast(self):
        return self._contrast

    @contrast.setter
    def contrast(self, contrast):
        self._contrast = contrast

    def __str__(self) -> str:
        return f"VideoEditor(contrast={self._contrast}, text={self.text})"
