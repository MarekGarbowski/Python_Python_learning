
# saldo = 10000
# klient_zweryfikowany = True
#
# if klient_zweryfikowany and saldo > 0:
#     print('masz kredyt')
# else:
#     print('niestety....')

print('=====')

# użytkownik = int(input('podaj kwotę do wypłaty: '))
# saldo = 10000
# klient_zweryfikowany = True
#
# if klient_zweryfikowany and saldo > 0 and saldo - użytkownik >= 0:
#     print('masz kredyt')
# else:
#     print('niestety, brakuje ci {} złotych'.format(użytkownik - saldo))

print('=========')
print()
print('Cwiczenie 4')
print()
# Podana jest zmienna tekstowa:
#
# fakt = 'python jest łatwy i przyjemny'
# Stwórz listę wszystkich znaków z podanej zmiennej fakt. Następnie wykorzystując zbiory,
# stwórz unikalny zbiór znaków z otrzymanej listy.
#
# Zbuduj instrukcję warunkową, która sprawdzi czy długość otrzymanego zbioru jest mniejsza niż 20 i
# wydrukuje informację "Mniej niż 20 unikalnych znaków.".
#
# W przeciwnej sytuacji wydrukuje "Liczba unikalnych znaków jest większa lub równa 20."

fakt = 'python jest łatwy i przyjemny'

fakt_list = fakt.replace(' ', '')
fakt_list = set(fakt_list)

if len(fakt_list) < 20:
    print('Mniej niż 20 unikalnych znaków')
else:
    print('Liczba unikalnych znaków jest większa lub równa 20.')
