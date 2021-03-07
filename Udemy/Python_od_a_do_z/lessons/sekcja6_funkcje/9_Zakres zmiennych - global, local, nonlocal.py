#
# i = 2
# j = i
# i = 3

a = 5


def fun_1():
    print(a)


fun_1()
print()
print('*' * 30)
print()

def fun_2():
    a = 3
    print(a)


fun_2()

print()
print('*' * 30)
print()

def fun_3():
    x = 3
    print(x)


fun_3()

print()
print('*' * 30)
print()

tech = 'Python'


def change_tech(new_tech):
    tech = new_tech
    print(tech)


print(tech)
change_tech('Java')
print(tech)

print()
print('*' * 30)
print()

techn = 'Python'


def change_tech(new_tech):
    global techn
    techn = new_tech
    print(techn)


print(techn)
change_tech('Java')
print(techn)

print()
print('*' * 30)
print()

level = 0


def f1():
    level = 1

    def f2():
        level = 2
        print('Funkcja f2: ', level)

    f2()
    print('Funkcja f1: ', level)
f1()
print('Globalnie: ', level)

print()
print('*' * 30)
print()

level1 = 0


def f3():
    level1 = 1

    def f4():
        nonlocal level1
        level1 = 2
        print('Funkcja f4: ', level1)

    f4()
    print('Funkcja f3: ', level1)


f3()
print('Globalnie: ', level1)

print()
print('*' * 30)
print()

level2 = 0


def f5():
    level2 = 1

    def f6():
        global level2
        level2 = 2
        print('Funkcja f6: ', level2)

    f6()
    print('Funkcja f5: ', level2)


f5()
print('Globalnie: ', level2)