# Podziel projekt - utwórz nowy pakiet shop i przenieś do osobnych modułów (plików) w pakiecie store:
#
# Klasę Apple
# Klasę Potato
# Klasę Product oraz funkcje generujące i wypisujące produkt
# Klasę Order oraz funkcje generujące i wypisujące zamówienie
# Utwórz skrypt uruchomieniowy main, który importuje i wykorzystuje powyższe klasy i funkcje

import store.order
import store.product
import store.apple
import store.potato
# from store.apple import Apple
# from store.potato import Potatoes


def run():
    green_apple = store.apple.Apple("green", "medium", 5.5)
    yellow_potato = store.potato.Potatoes("yellow", "small", 3.7)
    fresh_potato = store.potato.Potatoes("fresh", "big", 5)
    candy = store.product.Product("sweets", "food", 23)
    new_order = store.order.Order("Marek Garbowski", [candy])
    store.order.print_apple(green_apple)
    store.order.print_potato(yellow_potato)
    store.order.print_potato(fresh_potato)
    store.order.print_product(candy)
    store.order.print_order(new_order)


if __name__ == "__main__":
    run()
