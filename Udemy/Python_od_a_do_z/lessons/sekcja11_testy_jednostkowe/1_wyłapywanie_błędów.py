#  Najczęstsze błędy w Pythonie:

# print(1 / 0)  #  ZeroDivisionError: division by zero

# print(7 + '2')  #  TypeError: unsupported operand
# type(s) for +: 'int' and 'str'

# print(int('f'))  #  ValueError: invalid literal
# for int() with base 10: 'f'

#  Klauzula do obsługi błędów w Pythonie:

try:
    1 / 0
except:  #  W tym przykładzie wszystkie błędy trafią do tego komentarza
    print('Nie dzieli się przez "zero"!')

# W tym sposobie pisania każy typ błędu trafi do konkretnego wyjątku.

try:
    1 / '1'
except ZeroDivisionError:
    print('Nie dzieli się przez "zero"!')
except TypeError:
    print('Zły type!')


try:
    4 + '4'
except TypeError:
    print('Nie można dodawać tekstu do liczby')

try:
    int('oeru')
except ValueError:
    print('Zły tekst!')

while True:
    try:
        x = int(input('Podaj liczbę: '))
        break
    except ValueError:
        print('Nie wprowadziłeś poprawnej wartości.')

try:
    with open('test.txt', 'r') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print("Nie ma takiego pliku.")

# Raise - pozwala samemu podnosić typ błędu

# raise TypeError('Błąd')


def divide(x, y):
    try:
        x = int(x)
        y = int(y)
        return x / y
    except ZeroDivisionError:
        print('Nie można dzielić przez "Zero"!')
    except ValueError:
        print('Musisz wprowadzić liczbę.')


print(divide(2, 4))
print(divide(44, 0))
print(divide(2, 555))
print(divide(2, '6'))
print(divide(2, 'w'))
