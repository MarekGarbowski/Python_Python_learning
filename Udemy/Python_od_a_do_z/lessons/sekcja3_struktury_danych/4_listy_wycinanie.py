
list_1 = [34, 23, 12, 56]
ind_ng = [-4, -3, -2, -1]
index = [0, 1, 2, 3]

#  Lista [start:stop]
# Lista [index]
# Lista [start:]
#  Lista [:stop]
# Lista {::step]

print(list_1[0])
print(list_1[-1])
print(list_1[-3])

print(list_1[1:3])
print(list_1[-3:-1])
print(list_1[::-1])
print(list_1[::1])
print(list_1[:1])
print(list_1[:2])
print(list_1[:3])
print(list_1[:4])

print(list_1[:-1])
print(list_1[:-2])
print(list_1[:-3])
print(list_1[:-4])

print('Ćwiczenie 4')
# Stwórz zmienną techs i przypisz do niej listę podanych technologi:
#
# java
# python
# spark
# hadoop
# r
# Następnie wydrukuj do konsoli numer indeksu listy zawierający ciąg znaków 'python'

techs = ['java', 'python', 'spark', 'hadoop', 'r']
print(techs.index('python'))

# techs = ['java', 'python', 'spark', 'hadoop', 'r']
#
# print(1)
