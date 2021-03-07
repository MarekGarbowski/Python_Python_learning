#
#
stocks = {'amzn.us': 'amazon.com inc', 'googl.us': 'alphabet inc', 'aapl.us': 'apple inc', 'uber.us': 'uber techologies inc', 'msft.us': 'microsoft corp'}

print(stocks.keys())
print(stocks.values())
print(stocks.items())


for key, value in stocks.items():
    print('{}: {}'.format(key, value))

print()
print('*' * 30)
print()

# to samo tylko w dict comprehention

x = {key:value for (key, value) in stocks.items()}
print(x)

print()
print('*' * 30)
print()

xx = {(key1, value1) for (key1, value1) in stocks.items()}
print(xx)

print()
print('*' * 30)
print()

xxx = {value2:key2 for (key2, value2) in stocks.items()}
print(xxx)

print()
print('*' * 30)
print()

a = {(key3.capitalize(), value3.upper()) for (key3, value3) in stocks.items()}
print(a)

print()
print('*' * 30)
print()

ss = {key4:len(value4) for (key4, value4) in stocks.items()}
print(ss)

print()
print('*' * 30)
print()

sss = {key5:value5 + ':' + str(len(value5)) for (key5, value5) in stocks.items()}
print(sss)

print()
print('*' * 30)
print()

def replace_corp_inc(name):
    name = name.replace('corp', '0')
    name = name.replace('inc', '1')
    return name

cc = {k:replace_corp_inc(v) for (k, v) in stocks.items()}
print(cc)

print()
print('*' * 30)
print()

dd = {k1:v1 for (k1, v1) in stocks.items() if 'corp' in v1}
print(dd)

print()
print('*' * 30)
print()

ddd = {k1:v1 for (k1, v1) in stocks.items() if 'inc' in v1}
print(ddd)

print()
print('*' * 30)
print()

dddd = {k1:v1 for (k1, v1) in stocks.items()if v1.startswith('a')}
print(dddd)

print()
print('*' * 30)
print()

f = {k1:v1 for (k1, v1) in stocks.items()if len(v1) < 13}
print(f)

#  Ćwiczenie 2
#  Podany jest słownik:
#  
#  d = {'jeden': 1, 'dwa': 2, 'trzy': 3}
#  Wykorzystując dict comprehension zamień mapowanie tekstu na liczbę odpowiednio na liczbę na tekst. Wynik wydrukuj do konsoli.
#  
#  Uwaga: Zadanie można wykonać w jednej linii.

ds = {'jeden': 1, 'dwa': 2, 'trzy': 3}

sd = {value_1:key_1 for (key_1, value_1) in ds.items()}
print(sd)

print()
print('*' * 30)
print()

ff = {ke: 'corp' if 'corp' in va else 'inc' for (ke, va) in stocks.items()}
print(ff)


print()
print('*' * 30)
print()

numbers = range(20)

numbers_dict = {}

for number in numbers:
    if number % 2 == 0:
        numbers_dict[number] = number ** 2
print(numbers_dict)

print()
print('*' * 30)
print()

#  to  samo z dict comprehention

num = {k: k ** 2 for k in numbers if k % 2 == 0}
print(num)


nested_dict = {'001': {'price': 100},
               '002': {'price': 40},
               '003': {'price': 60}}

for key1, val1 in nested_dict.items():
    print(key1, val1['price'])


print()
print('*' * 30)
print()

nest = {key2:val2 for (key2, val2) in nested_dict.items()}
print(nest)

nest1 = {key3:val3['price'] for (key3, val3) in nested_dict.items()}
print(nest1)

nested_dict_1 = {'001': {'price': 100, 'items': 4},
               '002': {'price': 40, 'items': 9},
               '003': {'price': 60, 'items': 8}}

for key1, val1 in nested_dict_1.items():
    print(key1, val1)

print()
print('*' * 30)
print()

nest = {key2:val2 for (key2, val2) in nested_dict_1.items()}
print(nest)

nest2 = {key_1:val_1['price'] * val_1['items'] for (key_1, val_1) in nested_dict_1.items()}
print(nest2)

