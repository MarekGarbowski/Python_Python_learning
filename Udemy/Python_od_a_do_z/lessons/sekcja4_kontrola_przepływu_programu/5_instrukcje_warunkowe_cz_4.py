
name = 'python'
if 'p' in name:
    print('znaleziono literę')
else:
    print('nie znaleziono litery...')

print('=====')

tech = 'python'
if tech == 'python':
    flag = 'dobry wybór'
else:
    flag = 'poszukaj czegoś lepszego...'
print(flag)
print('=====')

#  x if [warunek] else y

flag = 'dobry wybór' if tech == 'python' else 'poszukaj czegoś innego...'
print(flag)
print('==========')
print()

print("Cwiczenie 5")
print()
# Dana jest zmienna tekstowa:
#
# long = 'sfdvjklncdnskjccbnksjdnckjsdsnckjnsdkjnckjsnkjlcnqdlknwsx'
# Korzystając z instrukcji warunkowej sprawdź czy zmienna long zawiera znak 'q'.
# Jeżeli tak, wydrukuj: 'Zawiera', w przeciwnym razie 'Nie zawiera'.

long = 'sfdvjklncdnskjccbnksjdnckjsdsnckjnsdkjnckjsnkjlcnqdlknwsx'
if 'q' in long:
    print('zawiera')
else:
    print('Nie zawiera')
