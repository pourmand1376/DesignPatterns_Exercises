class DataReader():
    def read(self, filename: str):
        if filename.endswith('.xls'):
            print('Reading data from an Excel spreadsheet.')
        elif filename.endswith('.numbers'):
            print('Reading data from a Numbers spreadsheet.')
        elif filename.endswith('.qbw'):
            print('Reading data from a QuickBooks file.')
        else:
            raise NotImplementedError()

reader = DataReader()
reader.read('test.xls')