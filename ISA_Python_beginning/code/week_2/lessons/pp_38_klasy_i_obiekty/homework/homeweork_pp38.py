# Utwórz klasy do reprezentacji Produktu, Zamówienia, Jabłek i Ziemniaków.
# Stwórz po kilka obiektów typu jabłko i ziemniak i wypisz ich typ za pomocą funkcji wbudowanej type.
# Stwórz listę zawierającą 5 zamówień oraz słownik, w którym kluczami będą nazwy produktów,
# a wartościami instancje klasy produkt.

class Product:
    pass


class Order:
    pass


class Apple:
    pass


class Potatoes:
    pass


if __name__ == '__main__':
    green_apple = Apple()
    red_apple = Apple()
    yellow_apple = Apple()
    vege = Potatoes(), Potatoes(), Potatoes(),Potatoes()
    print(type(green_apple))
    print(type(vege))
    orders = Order(), Order(), Order(), Order(), Order()
    print(orders)
    products = {
        "Jabłko": Product(),
        "Banany": Product(),
        "Pomarańcze": Product(),
        "Ananas": Product(),
    }
    print(products)
