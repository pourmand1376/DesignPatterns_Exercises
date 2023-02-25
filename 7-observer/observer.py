from components import Stock, StatusBar, StockListView
def main():
    stock1 = Stock('Amir',1000)
    stock2 = Stock('Sedighe', 100)
    stock3 = Stock('Hassan', 10)

    status_bar=StatusBar()
    status_bar.add_stock(stock1)
    status_bar.add_stock(stock2)

    stock_listview = StockListView()
    stock_listview.add_stock(stock2)
    stock_listview.add_stock(stock3)

    stock1.price = 500
    stock2.price = 700
    stock3.price = 800
    

if __name__ == '__main__':
    main()