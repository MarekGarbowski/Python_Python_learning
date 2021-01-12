
empty_list = list()
print(empty_list)

techs = ['Python', 'Java', 'C++', 'go']
print(techs)
print(techs[0])
techs[0] = "Python 3.7"
print(techs)

numbers = [1, 2, 3, 4, 5, 6]
print(numbers)
print(type(numbers))

mixed = [1, 3, 'Python', 2, 4, 3.7, True]
print(mixed)

empty = []
print(empty)
nested = [[1, 2, 3, 4], ['test', 'Python', 'Java'], 3]
print(nested)
empty = ['test']
print(empty)
print(type(empty))
empty = ['qwerty']
print(empty)
empty += ['test']
print(empty)

order_1 = ['mleko', 'ziemniaki', 'makaron']
order_2 = ['woda', 'jajka']

bucket = [order_1, order_1]
print(bucket)

# order_1 += order_2
print(order_1)

print(len(bucket))
full = order_1 + order_2 + ['kakao']
print(full)
full += ['ryż']
print(full)
print(dir(list))


# Ćwiczenie 3
# Stwórz dwie listy:
#
# numbers - zawierająca cyfry 1, 4, 2, 5
# letters - zawierająca litery d, s, t
# Następnie połącz te listy w jedną i wydrukuj do konsoli.

numbers = [1, 4, 2, 5]
letters = ['d', 's', 't']
print(letters + numbers)
letters += numbers
print(letters)
