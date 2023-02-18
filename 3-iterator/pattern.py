from collections.abc import Iterable,Iterator

class Product():
    def __init__(self,id:int, name:str) -> None:
        self.id = id
        self.name = name
    
    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}"

class ArrayIterator(Iterator):
    def __init__(self,items):
        self.items = items
        self._position = 0

    def __next__(self) :
        try:
            item = self.items[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return item

class ProductCollection(Iterable):
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)
    
    def __iter__(self):
        return ArrayIterator(self.items)

def main():
    products = ProductCollection()
    products.add(Product(1,"First"))
    products.add(Product(2,"Second"))
    products.add(Product(3,"Third"))

    for item in products:
        print(item)

if __name__ == "__main__":
    main()