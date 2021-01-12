
string = "Python"
print(dir(string))

a = 10
print(dir(a))

print(type(a))

b = 4.2
print(type(b))

c = 3 + 3j
print(type(c))
print(c)


d = True
print(type(d))

# Ćwiczenie 5
# Sprawdź jaki typ mają następujące zmienne:
#
# x = '1323435'
# y = 12334
# z = '0'
# Wynik podaj przy użyciu jednej funkcji print(). Oczekiwany rezultat:
#
# x: <class 'str'>
#
# y: <class 'int'>
#
# z: <class 'str'>

x = '1323435'
y = 12334
z = '0'
print('x:{}\ny:{}\nz:{}'.format(type(x), type(y), type(z)))
