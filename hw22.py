class Item:
    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name
    def __str__(self):
        return f'{self.name}, price: {self.price}'
class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone
    def __str__(self):
        return f'User: {self.name} {self.surname}'
class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0
    def add_item(self, item, cnt):
        self.products[item] = cnt
    def __str__(self):
        tmp = ''
        for item, cnt in self.products.items():
            tmp += f"{item.name}: {cnt} pcs.\n"
        return tmp
    def get_total(self):
        total = 0
        for key, cnt in self.products.items():
            total += key.price * cnt
        return total

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
