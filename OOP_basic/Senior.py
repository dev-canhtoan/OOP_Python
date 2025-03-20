class Product:
    def __init__(self,product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
class OrderItem:
    def __init__(self,product, quantity):
        self.product = product
        self.quantity = quantity
class Order:
    def __init__(self,order_id,items):
        self.order_id = order_id
        self.order_items = items
    def add_item(self, product, quantity):
