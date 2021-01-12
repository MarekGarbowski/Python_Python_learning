
empty_tuple = tuple()
print(empty_tuple)

amazon = ('amazon', 'USA', 'Technology', 1)
print(amazon)
print(type(amazon))
print(amazon[0])
google = ('Google', 'USA', 'Technology', 2)
print(google)

data = (amazon, google)
print(data)
print(type(data))

a = ('Marek', 'Garbowski')
print(a)
print(a[0])
name = "Marek"
surname = "Garbowski"

imie, nazwisko = ('Marek', 'Garbowski')
print(imie)
print(nazwisko)
print(imie, nazwisko)

amazon_name, country, sector, rank = amazon
print(amazon_name)
print(country,amazon_name)

stocks = 'Amazon', 'Apple', 'IBM'
print(type(stocks))
print(stocks)

nested = 'Europa', 'Polska', ('Warszawa', 'Kraków', 'Wrocław')
print(nested)
print(nested[2])

aa = 12
bb = 14
cc = bb
bb = aa
aa = cc
print(aa, bb)

x, y = 10, 15
x, y = y, x
print(x, y)


# Ćwiczenie 2
# Mamy podane zmienne:
#
# x = 'Python'
# y = 3.7
# Przedstaw te zmienne w postaci jednej tupli i wydrukuj do konsoli.

# xx, yy = 'Python', '3.7'
# print(xx, yy)

xx = 'Python'
yy = '3.7'
zz = (xx, yy)
print(zz)
print(type(zz))

aaa = tuple('123')
print(aaa)

aaaa = (1)
print(aaaa)
print(type(aaaa))
