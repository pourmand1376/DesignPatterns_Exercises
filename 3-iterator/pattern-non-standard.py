class Product():
    def __init__(self,id:int, name:str) -> None:
        self.id = id
        self.name = name
    
    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}"

class Iterator():
    def next():
        pass
    def has_next():
        pass
    def current():
        pass

class ArrayIterator(Iterator):
    def __init__(self,items):
        self.items = items
        self._position = 0

    def current(self):
        return self.items[self._position]
    def has_next(self):
        return self._position < len(self.items)
    def next(self) :
        self._position += 1

class ProductCollection():
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)
    
    def return_iterable(self):
        return ArrayIterator(self.items)

def main():
    products = ProductCollection()
    products.add(Product(1,"First"))
    products.add(Product(2,"Second"))
    products.add(Product(3,"Third"))

    products_iterable = products.return_iterable()
    while products_iterable.has_next():
        print(products_iterable.current())
        products_iterable.next()

if __name__ == "__main__":
    main()