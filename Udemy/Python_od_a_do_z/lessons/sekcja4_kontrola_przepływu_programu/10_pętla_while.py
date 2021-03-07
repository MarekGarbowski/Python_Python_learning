#
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#
# n = 0
# while True:
#     print(n)
#     if n >= 10:
#         break
#     n += 1
#
# while True:
#     name = input('Podaj swoje imię: ')
#     if len(name) >= 3 and name.isalpha():
#         break
# print(f'Cześć {name}!')
#
# print('=====')

# n = 0

# while n < 20:
#     n += 1
#     if n % 2 == 0:
#         continue
#     print(n)
# print('=====')


# lista = [12, 15, 45, 2198, 37]
# flag = False
# idx = 0
# value = 45
# while idx < len(lista):
#     print(lista[idx])
#     idx += 1
# print('=====')

# lista = [12, 15, 45, 2198, 37]
# flag = False
# idx = 0
# value = 45
#
# while idx < len(lista):
#     print(lista[idx])
#     if lista[idx] == value:
#         flag = True
#         print(flag)
#         break
#     idx += 1
# print('=====')

# lista = [12, 15, 45, 2198, 37]
# flag = False
# idx = 0
# value = 44
#
# while idx < len(lista):
#     print(lista[idx])
#     if lista[idx] == value:
#         flag = True
#         print(flag)
#         break
#     idx += 1
# if not flag:
#     lista.append(value)
#     print(lista)

print('=========')
print()
print('Cwiczenie 10')
print()

# Przeszukaj czy podana lista:
#
# [23, 12, 53, 13, 65, 1, 45]
# zawiera wartość 13.
#
# Skorzystaj z pętli while. Jeżeli wartość zostanie znaleziona wydrukuj 'Znaleziono'.

list = [23, 12, 53, 13, 65, 1, 45]
value = 13
number = 0

while number < len(list):
    if list[number] == value:
        print('Znaleziono!')
        break
    number += 1
