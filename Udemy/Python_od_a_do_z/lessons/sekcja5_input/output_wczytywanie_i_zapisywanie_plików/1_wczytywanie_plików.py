
file = open('simple.txt', 'r')

for line in file:
    print(line, end='')  # bez parametru end wydrukuje nam co drugą linie, parametr end kasuje nam puste linie

file.close()
print('=====')

with open('simple.txt', 'r') as file:  # robi to co program powyżej z automatycznym zamknieciem pliku
    for line in file:
        print(line, end='')


# Funkcja open(file, mode) pozwala otworzyć plik i zwraca go jako obiekt.
#
# Najczęściej stosowane tryby otwierania plików:
#
# 'r' - read - otwiera plik do odczytu, zwraca błąd jeśli plik nie istnieje
# 'a' - append - otwiera plik do dopisania, tworzy plik jeśli nie istnieje
# 'w' - write - otwiera plik do zapisu, tworzy plik jeśli nie istnieje

print('=========')
print()

print('Cwiczenie 1')
print()

# Odczytaj podany plik data.txt zawierający dane dotyczące notowań trzech spółek.
#
# Wydrukuj każdą linię do konsoli.
#
# Wskazówka: Użyj parametru end='' w funkcji print()

with open('data.txt', 'r') as file:
    for line in file:
        print(line, end='')
