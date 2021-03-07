
# def print_even(maximum):
#     even = []
#     for i in range(maximum + 1):
#         if i % 2 == 0:
#             even.append(i)
#     return even
#
#
# print_even(10)
# num = print_even(20)
# print(num)


# def write_file(file_name, text):
#     with open(file_name, 'w') as file:
#         print(text, file=file)
#
#
# write_file('sample.txt', 'Pierwsza linia.\nDruga linia.')
# write_file('sample2.txt', 'pierwsza.\ndruga.\ntrzecia')

# def calculate_profit(pv, rate, n):
#     return pv * (1 + rate)**n - pv
#
#
# print(calculate_profit(1000, 0.2, 15))


# def calculate_profit(pv=1000, rate=0.03, n=1):  # funkcja z parametrami domyślnymi
#     return pv * (1 + rate)**n - pv
#
#
# print(calculate_profit())

# def calculate_profit(pv=1000, rate=0.03, n=1):  # nadpisanie domyślnego parametru nową wartością
#     return pv * (1 + rate)**n - pv
#
#
# print(calculate_profit(rate=0.3))


# Ćwiczenie 3
# Napisz funkcję drukuj_nieparzyste, która zwróci listę liczb nieparzystych większych od zera i mniejszych od 20.
#
# Oczekiwany rezultat: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#
# Uwaga: Do oceny zadania wystarczy samo zdefiniowanie funkcji, nie trzeba jej wywoływać.


def drukuj_nieparzyste(maximum):
    even = []
    for i in range(maximum):
        if i % 2 != 0:
            even.append(i)
    return even


print(drukuj_nieparzyste(20))
