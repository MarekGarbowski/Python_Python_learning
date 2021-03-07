
# def funkcja_2(**kwargs):
#     for kwarg in kwargs:
#         print(kwarg)
#
#
# funkcja_2(**{'a':1, 'b':2})

# def fun(**kwargs):
#     print(kwargs)
#
#
# fun(a=1, b=4)
# fun(x1=10, x2=20, x3=30)

# def fun_2(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# fun_2(1, 2, 3, a=10, b=12)

# def fun_2(*args, **kwargs):
#     print(sum(args))
#     print(kwargs.values())
#
#
# fun_2(1, 2, 3, a=10, b=12, c=14)


# Ćwiczenie 6
# Napisz funkcję policz_kwargs , która zwróci liczbę przekazanych tzw. 'keyword argument' (argumentów, które podajemy przy pomocy nazwy zmiennej) podczas wywołania funkcji.
#
#
#
# Przykład:
#
# policz_kwargs(a=1, b=2, c=3) -> 3
# policz_kwargs(10, a=1, b=2) -> 2

def policz_kwargs(*args, **kwargs):
    print(len(kwargs))


policz_kwargs(a=1, b=2, c=3)
policz_kwargs(10, a=1, b=2)
