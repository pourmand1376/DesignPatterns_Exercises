class Stock:
    def __init__(self, symbol, price):
        self.observers = []
        self.symbol = symbol
        self.price = price

    def __str__(self) -> str:
        return f"Symbol: {self.symbol}, Price: {self.price}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        self.notifiy_observers(value)

    def notifiy_observers(self,value):
        for observer in self.observers:
            observer.update(value)
    
class StatusBar():
    def __init__(self):
        self.stocks = []
    
    def add_stock(self, stock:Stock):
        self.stocks.append(stock)
        stock.observers.append(self)
    
    def show(self):
        for stock in self.stocks:
            print(stock)
    
    def update(self,value):
        print(f"StatusBar notified of update {value}")


class StockListView:
    def __init__(self):
        self.stocks = []
    
    def add_stock(self, stock:Stock):
        self.stocks.append(stock)
        stock.observers.append(self)
    
    def show(self):
        for stock in self.stocks:
            print(stock)

    def update(self,value):
        print(f"StockListView notified about update {value}")