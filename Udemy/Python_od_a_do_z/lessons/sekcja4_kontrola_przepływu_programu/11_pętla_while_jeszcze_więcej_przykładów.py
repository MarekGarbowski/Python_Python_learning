
pin_code = "0000"
a = False
b = 1
c = False

pin = input("podaj kod pin: ")
while pin != pin_code and b < 3:
    pin = input("podaj kod pin: ")
    b += 1
    if b == 3:
        c = True
if not c:
    new = input("chcesz zmienić swój pin? ")
    if new == "tak":
        new_pin = input('podaj nowy pin: ')
        pin_code = new_pin
        print('zmieniono pin')
        a = True
    if a:
        print('zalogowano z nowym kodem')
    else:
        print('zalogowano z starym kodem')
else:
    print('Nie podano poprawnego kodu pin')

print('=====')
print()
