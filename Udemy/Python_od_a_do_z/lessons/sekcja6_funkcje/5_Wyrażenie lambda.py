# definiowanie funkcji za pomocą jednej linii

# standardowa funkcja, z przypisaniem do innej zmiennej


# def parabola(x):
#     return x ** 2
#
#
# print(type(parabola))
#
# print(parabola(30))
#
# funkcja_1 = parabola
# print(type(funkcja_1))
#
# print(funkcja_1(30))

# przypisanie funkcji napisanej w jednej linii do zmiennej
# f = lambda x: x ** 2 + 3
# print(f(30))
#
# f_2 = lambda word: word.upper()
#
# print(f_2('python'))
#
# f_3 = lambda x, y: x + y
#
# print(f_3(3, 5))
#
# f_4 = lambda word_1, word_2: word_1 + word_2
#
# print(f_4('hello ', 'world'))
#
# lista = ['python', 'java', 'r', 'sql']
# print(list(map(lambda word: word.upper(), lista)))
#
#
# def make_upper(word):
#     return word.upper()
#
#
# print(list(map(make_upper, lista)))


# print(list(map(lambda word: word.title(), lista)))

# print(list(map(lambda word: (word, len(word)), lista)))

# def apply_func(x, fn):
#     return fn(x)
#
#
# print(apply_func(5, lambda x: x ** 2))
# print(apply_func([12, 42], lambda x: sum(x)))

# numbers = [6, 4, 2, 7, 9]
# print(sorted(numbers))

# numbers = [-3, -2, -1, 0, 1, 2, 3]
# print(sorted(numbers, key = lambda x: abs(x)))

# list_1 = [('jeden', 'one'), ('dwa', 'two'), ('trzy', 'three')]
#
# print(sorted(list_1))
# print(sorted(list_1, key=lambda x: x[1]))


# Ćwiczenie 4
# Podana jest lista miast:
#
# cities = ['Warsaw', 'London', 'Berlin', 'New York']
# Używając funkcji map() oraz wyrażenia lambda uzyskaj listę zawierającą trzy pierwsze litery każdego miasta.
#
# Otrzymaną listę wydrukuj do konsoli.

cities = ['Warsaw', 'London', 'Berlin', 'New York']

print(list(map(lambda city: city[0:3], cities)))
