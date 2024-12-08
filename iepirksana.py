class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        total_price = self.price * self.quantity
        print(f"Product: {self.name}, Total Price: {total_price:.2f}")
        return total_price


product1 = Product("Apple", 0.7, 10)
product2 = Product("Banana", 0.4, 15)


product1.get_total_price()
product2.get_total_price()

product1.get_total_price()
product2.get_total_pr
