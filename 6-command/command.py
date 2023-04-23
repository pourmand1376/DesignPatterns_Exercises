from abc import ABC, abstractmethod
from video import VideoEditor

class Command(ABC):
    @abstractmethod
    def execute(self, arg):
        pass

class UndoableCommand(Command):
    @abstractmethod
    def unexecute(self):
        pass

class History():
    def __init__(self):
        self.commands = []
    
    def pop(self):
        return self.commands.pop()

    def push(self, command:Command):
        self.commands.append(command)

    def __len__(self):
        return len(self.commands)

class ContrastCommand(UndoableCommand):
    def __init__(self, video_editor:VideoEditor, history:History):
        self.video_editor = video_editor
        self.history = history
        self.previous_contrast = self.video_editor.contrast

    def execute(self, contrast):
        self.previous_contrast = self.video_editor.contrast
        self.video_editor.contrast = contrast
        self.history.push(self)
        print(f'contrast is set to {contrast}')

    def unexecute(self):
        self.video_editor.contrast = self.previous_contrast
        print(f'contrast is set to {self.previous_contrast}')

class TextCommand(UndoableCommand):
    def __init__(self, video_editor:VideoEditor, history:History):
        self.video_editor = video_editor
        self.history = history
        self.previous_text = self.video_editor.text

    def execute(self, text):
        self.previous_text = self.video_editor.text
        self.video_editor.text = text
        self.history.push(self)
        print(f'text is set to {text}')

    def unexecute(self):
        self.video_editor.text = self.previous_text
        print(f'text is set to {self.previous_text}')

class UndoCommand(Command):
    def __init__(self, history):
        self.history = history
    
    def execute(self, arg=None):
        if len(self.history) > 0:
            print('executing undo command')
            self.history.pop().unexecute()

history = History()
video_editor = VideoEditor()
contrast_command = ContrastCommand(video_editor=video_editor, history=history)
text_command = TextCommand(video_editor=video_editor, history=history)

contrast_command.execute(0.3)
text_command.execute('amir')
contrast_command.execute(1)
text_command.execute('hasan')

undoCommand = UndoCommand(history=history)
undoCommand.execute()
undoCommand.execute()