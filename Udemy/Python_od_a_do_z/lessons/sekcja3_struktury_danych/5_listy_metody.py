
techs = []
print(techs)

techs.append('python')
print(techs)
techs.append('Java')
print(techs)
# techs.append(['hadoop', 'spark'])
print(techs)
techs.extend(['sql', 'sas'])
print(techs)
techs.insert(2, 'go')
print(techs)
techs.insert(1, 'r')
print(techs)
techs.pop()
print(techs)
techs.pop()
print(techs)
techs.pop(1)
print(techs)

techs = ['python', 'java', 'sql', 'php', 'python']
print(techs.index('java'))
print(techs.index('php'))

print(techs.count('python'))

techs.sort()
print(techs)

techs.reverse()
print(techs)

techs[1] = 'C++'
print(techs)

print('Cwiczenie 5')
# Podane są dwie listy:
#
# [4, 5, 3, 3]
# [9, 7]
# Używając odpowiedniej metody połącz te dwie listy w jedną i wydrukuj do konsoli.

a = [4, 5, 3, 3]
b = [9, 7]
a.extend(b)
print(a)

print('Cwiczenie 6')
# Podane są następujące elementy: 'Apple', 'Microsoft', 'Samsung', 'Netflix', 'Uber'.
#
# Z podanych elementów utwórz listę. Używając odpowiedniej metody dodaj jeszcze dwa elementy na koniec listy:
# 'Amazon', 'Google'
#
# Wydrukuj otrzymaną listę do konsoli

list_1 = ['Apple', 'Microsoft', 'Samsung', 'Netflix', 'Uber']
list_1.append('Amazon')
list_1.append('Google')
print(list_1)
