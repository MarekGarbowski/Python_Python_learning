# # Napisz funkcję generującą zamówienie z losową listą produktów na przykład: Produkt-1, Produkt-2 itd
#
# import random
#
#
# class Product:
#     def __init__(self, name, category_name, price_per_unit):
#         self.name = name
#         self.category_name = category_name
#         self.price_per_unit = price_per_unit
#
#
# class Order:
#     def __init__(self, full_name, product_list=None):
#         self.full_name = full_name
#         if product_list is None:
#             product_list = []
#         self.product_list = product_list
#
#         total_price = 0
#         for product in product_list:
#             total_price += product.price_per_unit
#         self.total_price = total_price
#
#
# class Apple:
#     def __init__(self, name, size, price_per_kg):
#         self.name = name
#         self.size = size
#         self.price_per_kg = price_per_kg
#
#
# class Potatoes:
#     def __init__(self, name, size, price_per_kg):
#         self.name = name
#         self.size = size
#         self.price_per_kg = price_per_kg
#
#
# def print_product(product):
#     print(f"Product: {product.name}, {product.category_name}, price: {product.price_per_unit}")
#
#
# def print_apple(apple):
#     print(f"Product: {apple.name}, {apple.size}, price: {apple.price_per_kg}")
#
#
# def print_potato(potato):
#     print(f"Product: {potato.name}, {potato.size}, price: {potato.price_per_kg}")
#
#
# def print_order(order):
#     print(f"zamówienie złożone przez: {order.full_name}")
#     print(f"o łącznej wartości: {order.total_price} PLN")
#     print("Zamówione produkty:")
#     for product in order.product_list:
#         print("\t", end="")
#         print_product(product)
#         print("=" * 20)
#         print()
#
#
# def run():
#     new_order = create_order_list()
#     print_order(new_order)
#     # green_apple = Apple("green", "medium", 5.5)
#     # yellow_potato = Potatoes("yellow", "small", 3.7)
#     # fresh_potato = Potatoes("fresh", "big", 5)
#     # candy = Product("sweets", "food", 23)
#     # new_order = Order("Marek Garbowski", [candy])
#     # print_apple(green_apple)
#     # print_potato(yellow_potato)
#     # print_potato(fresh_potato)
#     # print_product(candy)
#     # print_order(new_order)
#
#
# def create_order_list():
#     number_of_products = random.randint(1, 10)
#     products = []
#     for product_number in range(number_of_products):
#         product_name = f"Produkt-{product_number}"
#         category_name = "inne"
#         unit_price = random.randint(1, 100)
#         product = Product(product_name, category_name, unit_price)
#         products.append(product)
#
#     order = Order(full_name="Marek", product_list=products)
#     return order
#
#
# if __name__ == "__main__":
#     run()
