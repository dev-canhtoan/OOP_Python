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
        new_item = OrderItem(product, quantity)
        self.order_items.append(new_item)
        print(f"Đã thêm {quantity}- {product.name} vào đơn hàng {self.order_id}")
    def caculate_total(self):
        total = sum(item.product.price * item.quantity for item in self.order_items)
        return total
    def display_order(self):
        print(f"Chi tiết đơn hàng: {self.order_id}")
        print(f"Danh sách sản phẩm: ")
        for item in self.order_items:
            print(f"{item.product.name}: {item.quantity} x {item.product.price} = {item.product.price * item.quantity}")
        print(f"Tổng tiền: {self.caculate_total()}vnd")
p1 = Product(1, "Laptop", 15000000)
p2 = Product(2, "Chuột không dây", 500000)

order = Order("DH001", [])

order.add_item(p1, 2)
order.add_item(p2, 1)

order.display_order()

