
# def test_args(x, *args):
#     print('Pierwszy parametr: ', x)
#     for arg in args:
#         print('Kolejny parametr *args: ', arg)
#
#
# test_args(4, 3, 4, 2, 54, 7, 234, 345)

# def function_1(x, y, *args):
#     print('x= ', x)
#     print('y= ', y)
#     print('args= ', args)
#
#
# function_1(1, 2)
# function_1(1, 2, 3)
# function_1(1, 2, 3, 4, 5, 6)

# def suma(x, y):
#     return x + y
#
# def suma_dowol(*args):
#     return sum(args)
#
#
# print(suma(1, 2))
# print(suma_dowol(1, 2))
# print(suma_dowol(1, 2, 3))
# print(suma_dowol(1, 2, 3, 4))


# Ćwiczenie 5
# Napisz funkcję policz_srednia, która policzy średnią dowolnej liczby przekazanych argumentów.

def aritmetic(*args):
    return sum(args)/len(args)


print(aritmetic(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(aritmetic(1, 2, 3))

