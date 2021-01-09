# from product import Product
# from apple import Apple
# from potato import Potatoes


class Order:
    def __init__(self, full_name, product_list=None):
        self.full_name = full_name
        if product_list is None:
            product_list = []
        self.product_list = product_list

        total_price = 0
        for product in product_list:
            total_price += product.price_per_unit
        self.total_price = total_price


def print_product(product):
    print(f"Product: {product.name}, {product.category_name}, price: {product.price_per_unit}")

#
def print_apple(apple):
    print(f"Product: {apple.name}, {apple.size}, price: {apple.price_per_kg}")


def print_potato(potato):
    print(f"Product: {potato.name}, {potato.size}, price: {potato.price_per_kg}")


def print_order(order):
    print(f"zamówienie złożone przez: {order.full_name}")
    print(f"o łącznej wartości: {order.total_price} PLN")
    print("Zamówione produkty:")
    for product in order.product_list:
        # print("\t", end="")
        print("=" * 20)
        print_product(product)
        print("=" * 20)
        print()
