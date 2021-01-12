
empty_set = set()
print(empty_set)
print(type(empty_set))

techs = {'python', 'java', 'c++', 'sql'}  # zbiór
print(techs)
print(type(techs))
dict_1 = {"1": 1, "2": 2}  # słownik
print(dict_1)
print(type(dict_1))
print(len(techs))

print(set('python'))
print(set('aaals'))

print('python' in techs)
print('go' in techs)

print(dir(set))

techs.add('sas')
print(techs)

techs.remove('sas')
print(techs)

techs.pop()
print(techs)

techs.clear()
print(techs)

A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9}
C = {5, 6}

print(C.issubset(A))
print(C.issubset(B))
print(B.issubset(A))
print(A.issuperset(B))
print(A.issuperset(C))
print(A.union(B))
print(A.intersection(B))
print(A.symmetric_difference(B))
D = A.copy()
print(D)

# Ćwiczenie 1
# Mamy podaną zmienną tekstową:
#
# x = 'Programowanie w języku Python - od A do Z'
# Używając odpowiednich metod zamień wszystkie znaki na małe litery, następnie zamień '-' oraz ' ' (spacja)
# na pusty ciąg znaków '', a także polskie litery na ich odpowiedniki (np. 'ą' -> 'a', 'ć' -> 'c').
#
# Użyj zbioru do wygenerowania unikalnych znaków i następnie podaj liczbę wszystkich unikalnych znaków
# w podanej zmiennej x. Wydrukuj wynik do konsoli.

x = 'Programowanie w języku Python - od A do Z'
print(type(x))
x = x.lower().replace('-', '').replace(' ', '').replace('ę', 'e')
print(x)
print(len(x))
print(len(set(x)))  # ta komenda nie zamienia zmienej w zbiór
print(x)
y = set(x)
print(y)
print(type(y))
# x = set(x)
# print(x)
print(len(y))
