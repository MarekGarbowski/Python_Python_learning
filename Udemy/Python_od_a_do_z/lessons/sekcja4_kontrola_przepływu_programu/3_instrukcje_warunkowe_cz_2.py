
# print('Program uruchomiony...')
# print("""Włam sie do systemu zgadujac dwucyfrowy kod pin.
# Numer składa się z cyfr 0,1,2.""")
#
# pin = input("Wprowadź numer pin: ")
# if pin == '21':
#     print('Brawo! Pin poprawny!')
# elif pin == '20':
#     print('Jesteś blisko....')
# else:
#     print('Nie zgadłeś....')
# print('=========')
#
# print('Program uruchomiony...')
# print("""Włam sie do systemu zgadujac dwucyfrowy kod pin.
# Numer składa się z cyfr 0,1,2.""")
#
# pin_1 = int(input("Wprowadź numer pin: "))
# if pin_1 == 21:
#     print('Brawo! Pin poprawny!')
# elif pin_1 == 20:
#     print('Jesteś blisko....')
# else:
#     print('Nie zgadłeś....')
# print('=====')

string = ' '
if string:
    print('nie pusty ciąg znaków')
else:
    print('pusty ciąg znaków')

number = 1
if number:
    print('liczba różna od zera')
else:
    print('Zero...')
print('=====')

default_flag = True
if not default_flag:
    print('nie doszło do zdarzenia')
else:
    print('doszło do zdarzenia')
print('=========')

print('Cwiczenie 3')
print()
# Zmienna
#
# v = 55 km/h
# oznacza prędkość poruszającego się pojazdu. Utwórz instrukcję warunkową,
# która sprawdzi czy poruszasz się za szybko w terenie zabudowanym (> 50 km/h).
#
# Jeżeli tak, wydrukuj do konsoli informację 'Zwolnij!', w przeciwnym razie 'Tak trzymaj!'.

v = 55
if v > 50:
    print('Zwolnij!')
else:
    print('Tak trzymaj')
