from abc import ABC, abstractmethod
class BaseWindow(ABC):
    def close(self):
        self.before_close()
        self._do_close()
        self.after_close()

    def before_close(self):
        pass
    def after_close(self):
        pass

    @abstractmethod
    def _do_close(self):
        pass

class Window(BaseWindow):
    def _do_close(self):
        print('close my window')

class OtherWindow(BaseWindow):
    def _do_close(self):
        print('close my other window')
    
    def before_close(self):
        print('before close my other window')

def main():
    window =Window()
    window.close()

    otherWindow = OtherWindow()
    otherWindow.close()

if __name__ == '__main__':
    main()