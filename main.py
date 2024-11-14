class Product:
    def __init__(self, name, price, spare, cotegory):
        self.name = name
        self.price = price
        self.spare = spare
        self.cotegory = cotegory

    def add_product(self, name, price, amount):
        if self.name == name:
            self.spare += amount
            print(f"{name} mavjud. Miqdor yangilandi. Yangi miqdor: {self.spare}")
        else:
            self.name = name
            self.price = price
            self.spare = amount
            print(f"Yangi tovar qo'shildi: {name}, Narxi: {price}, Miqdor: {amount}")

    def take_product(self, amount):
        if amount <= self.spare:
            self.spare -= amount
        else:
            print(f"Bu maxsulotdan {amount} mavjud!")



class Book(Product):
    def __init__(self, name, price, spare, cotegory, author, ganre, pages):
        super().__init__(name, price, spare, cotegory)
        self.author = author
        self.ganre = ganre
        self.pages = pages


class Clothes(Product):
    def __init__(self, name, price, spare, cotegory, size):
        super().__init__(name, price, spare, cotegory)
        self.size = size


class Electronics(Product):
    def __init__(self, name, price, spare, cotegory, brand):
        super().__init__(name, price, spare, cotegory)
        self.brand = brand


class Cart:
    def __init__(self):
        self.products = []
        self.total_price = 0

    def add_product(self, product, quantity):
        self.products.append((product, quantity))
        self.total_price += product.price * quantity

    def show_total_price(self):
        print(f"Total price: {self.total_price}")

    def order(self):
        for product, quantity in self.products:
            if product.take_product(quantity):
                self.total_price -= product.price * quantity
        print(f"Order placed successfully. Total price: {self.total_price}")
        self.products = []  
        self.total_price = 0 


book = Book("Python Programming", 30, 10, "Books", "John Doe", "Programming", 200)
clothes = Clothes("T-Shirt", 15, 50, "Clothes", "L")
electronics = Electronics("Laptop", 1000, 5, "Electronics", "Brand X")

cart = Cart()
cart.add_product(book, 2)
cart.add_product(clothes, 3)
cart.show_total_price()

cart.order()

