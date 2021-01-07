
# Dodaj konstruktor przyjmujący odpowiednie argumenty do klas Product, Order, Apple i Potato:
#
# Product: nazwa, nazwa kategorii, cena jednostkowa

# Order: imię i nazwisko zamawiającego, lista produktów (domyślnie pusta),
# łączna cena (obliczona w konstruktorze jako suma cen jednostkowych z listy produktów)

# Apple: nazwa gatunku, rozmiar, cena za kg

# Potato: nazwa gatunku, rozmiar, cena za kg

# Utwórz kilka obiektów każdej klasy


class Product:
    def __init__(self, name, category_name, price_per_unit):
        self.name = name
        self.category_name = category_name
        self.price_per_unit = price_per_unit


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


class Apple:
    def __init__(self, name, size, price_per_kg):
        self.name = name
        self.size = size
        self.price_per_kg = price_per_kg


class Potatoes:
    def __init__(self, name, size, price_per_kg):
        self.name = name
        self.size = size
        self.price_per_kg = price_per_kg


def run():
    green_apple = Apple("green", "medium", 5.5)
    yellow_potato = Potatoes("yellow", "small", 3.7)
    fresh_potato = Potatoes("fresh", "big", 5)
    candy = Product("sweets", "food", 23)
    new_order = Order("Marek Garbowski", [candy])
    print(green_apple.name, green_apple)
    print(yellow_potato.name, yellow_potato)
    print(fresh_potato.name, fresh_potato)
    print(candy)
    print(new_order)


if __name__ == "__main__":
    run()
