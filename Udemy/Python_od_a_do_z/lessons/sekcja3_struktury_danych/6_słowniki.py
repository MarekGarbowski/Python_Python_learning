
# dictionary = {'key':'value', 'key1':'value1'}

empty_dict = dict()
print(empty_dict)

d = {}
print(type(d))

dict_1 = {'jeden': 'one', 'dwa': 'two', 'trzy': 'three'}
print(dict_1)

dick_2 = {'jeden': 1, 'dwa': 2, 'trzy': 3}
print(dick_2)
print(len(dict_1))

dict_1['cztery'] = 'four'
print(dict_1)

# dict_1.clear()
# print(dict_1)

dict_12 = dict_1.copy()
print(dict_12)

print(dict_1.keys())
print(list(dict_1.keys()))

print(dict_1.values())
print(list(dict_1.values()))

print(dict_1.items())
print(list(dict_1.items()))

print(dict_1['jeden'])
print(dict_1.get('dwa'))
print(dict_1.get('dfa', 'tego nie ma na liście'))

# dict_1.pop('dwa')
# print(dict_1)
#
# print(dict_1.popitem())
# print(dict_1)

dict_1.update({'jeden': 1})
print(dict_1)

print('Cwiczenie 7')
# Utwórz słownik, który zmapuje pierwsze pięć liczb naturalnych na ich kwadraty (rozpocznij od 1).
#
# Przykład:
#
# key: value
#
# {3:9}
#
# Otrzymany słownik wydrukuj do konsoli.

square = {1: 1, 2: 4, 3: 9, 4: 16}
print(square)

print('Cwiczenie 8')
# Podany jest słownik:
#
# data = {'Polska': 'Warszawa', 'Niemcy': 'Berlin', 'Czechy': 'Praga'}
#
# Dodaj kolejny element do słownika: 'Włochy': 'Rzym'
#
# Następnie utwórz listę stolice i przypisz do niej posortowane od a do z nazwy stolic.
#
# Wynik sortowania wydrukuj do konsoli.

data = {'Polska': 'Warszawa', 'Niemcy': 'Berlin', 'Czechy': 'Praga'}
data['Włochy'] = 'Rzym'
print(data)
stolice = data.values()
print(stolice)
stolice = list(stolice)
print(stolice)
print(sorted(stolice))
