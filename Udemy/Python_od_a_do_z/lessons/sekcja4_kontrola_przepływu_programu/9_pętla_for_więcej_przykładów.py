
raw_data = '345!23!456!35'
clean_data = ''
for digit in raw_data:
    if digit == '!':
        clean_data += ','
        continue
    clean_data += digit
print(clean_data)
print('=====')
print()

for digit in raw_data:
    if digit != "!":
        clean_data += digit
    else:
        clean_data += ','
print(clean_data)

print('=====')
print('')

sum = 0
for i in range(10):
    sum += i
print(sum)

print('=====')
print()

saldo = 450
print('saldo początkowe: {} PLN'.format(saldo))
for kwota in range(10, 60, 10):
    print('wypłacona kwota{}'.format(kwota))
    saldo -= kwota
    print('saldo: {}'.format(saldo))
print('saldo końcowe: {}'.format(saldo))

print('=====')
print()

nick = input('Podaj swój nick:\n')
password = input(f'Podaj kod dostępu {nick}:\n')
# for dig in password:
#     if dig not in '0123456789' or len(password) > 4:
#         print(f'Kod nie poprawny {nick}!')
#         break
# else:
#     print(f'Kod poprawny {nick}!')

# druga wersja tego samego programu sprawdzająca na samym początku czy długość kodu pin jest odpowiednia
if len(password) == 4:
    for dig in password:
        if dig not in '0123456789':
            print(f'Kod nie poprawny {nick}!')
            break
    else:
        print(f'Kod poprawny {nick}!')
else:
    print(f'Kod nie poprawny {nick}!')
print('==========')
print('=========')

