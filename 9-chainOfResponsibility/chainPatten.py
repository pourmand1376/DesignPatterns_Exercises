class DataReader():
    def __init__(self,extension:str):
        self.next = None
        self.extension = extension
        
    def _doHandle(self, filename):
        pass

    def handle(self,filename):
        # returning true means finished
        if filename.endswith(self.extension):
            self._doHandle(filename)

        if self.next is not None:
            self.next.handle(filename)
    
    def set_next(self, next):
        original_object = self
        while self.next is not None:
            self = self.next
        self.next = next
        return original_object
        

class XLSDataReader(DataReader):
    def __init__(self):
        super().__init__('.xls')

    def _doHandle(self, filename):
        print('Reading data from an Excel spreadsheet.')

    def __str__(self) -> str:
        return 'This is excel spreadsheet handler'

class NumbersDataReader(DataReader):
    def __init__(self):
        super().__init__('.numbers')

    def _doHandle(self, filename):
        print('Reading data from a Numbers spreadsheet.')
    
    def __str__(self) -> str:
        return 'this is numbers spreadsheet handler'

class QBWDataReader(DataReader):
    def __init__(self):
        super().__init__('.qbw')

    def _doHandle(self, filename):
        print('Reading data from a QuickBooks file.')

    def __str__(self) -> str:
        return 'this is a QBW handler'

filename = 'myfile.xls'
my_handler=XLSDataReader() \
            .set_next(NumbersDataReader()) \
            .set_next(QBWDataReader())

my_handler.handle(filename)