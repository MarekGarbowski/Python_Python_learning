
version = 3.7
print(version)

print(version > 3)
print(version <= 3)

number = 1200
print(number > 1000)
print(number == 1200)
print(number == 2)

print(number != 1200)
print(number != 2)
print('=====')

# if [warunek] :
#     [instrukcje]

if number > 100:
    print('test')

if 8 < 10:
    print('tak')

if 8 > 10:
    print('tak')
print('=====')

a = 2
if a > 10:
    print('a>10')
else:
    print('a<10')
print('=====')

age = 12
if age < 18:
    print('nie masz uprawnień')
else:
    print('masz uprawnienia')
print('=====')

age_1 = 111
if age_1 == 18:
    print('masz 18 lat')
elif age_1 < 18:
    print('nie masz uprawnień')
else:  # można też napisać zamiast else: elif age_1 > 18
    print('dostęp przyznany')
print('=====')

age_2 = int(input('Podaj swój wiek: '))
if age_2 == 18:
    print('masz 18 lat')
elif age_2 < 18:
    print('nie masz uprawnień')
else:  # można też napisać zamiast else: elif age_1 > 18
    print('dostęp przyznany')
print('==========')
print('Cwiczenie 2')
# Stwórz instrukcję warunkową, która sprawdzi czy podana zmienna
#
# x = 10
# jest większa od zera. Jeżeli tak, wydrukuj do konsoli: 'Zmienna x większa od zera'.

x = 10
if x > 0:
    print('Zmienna x większa od zera')
