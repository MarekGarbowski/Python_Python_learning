#  projekt: "Magazyn"
import sys


class Magazine:

    def __init__(self, product_list):
        self.product_list = product_list

    def print_available_product(self):
        print('Dostępne produkty:')
        print()
        for product in self.product_list:
            print(product)
        print()

    def add_product(self):
        self.product_name = input('Podaj nazwę produktu: ')
        if self.product_name not in self.product_list:
            self.product_list.append(self.product_name)
        print()
        print(f'Produkt: "{self.product_name}", został dodany do magazynu.')
        print()

    def delete_product(self):
        self.product_name = input('Podaj nazwę produktu który chesz usunąć: ')
        if self.product_name in self.product_list:
            self.product_list.remove(self.product_name)
            print()
            print(f'Usunięto produkt: "{self.product_name}" z magazynu.')
            print()
        else:
            print()
            print(f'Podanego produktu: "{self.product_name}", nie ma na magazynie.')
            print()


magazine_1 = Magazine(['mleko', 'woda', 'jajka', 'masło'])
while True:
    print('-' * 10)
    print('Wprowadź "1" aby wyświetlić stan magazynu.')
    print('Wprowadź "2" aby dodać produkt.')
    print('Wprowadź "3" aby usunąć produkt.')
    print('Wprowadź "4" aby zakończyć program.')
    print('-' * 10)

    user_choice = int(input('>>>'))

    if user_choice == 1:
        magazine_1.print_available_product()
    elif user_choice == 2:
        magazine_1.add_product()
    elif user_choice == 3:
        magazine_1.delete_product()
    elif user_choice == 4:
        sys.exit()
