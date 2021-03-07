
for i in '0123456789':
    if i == '6':
        print(i)
        break
    print(i, type(i))
print('koniec')
print('=====')

sample = 'python course'
for l in sample:
    if l == ' ':
        break
    print(l)
print('=====')

for char in 'kowalskij@gmail.com':
    if char == '@':
        print('adres email zweryfikowany')
        break
else:
    print('niepoprawny adres email')
print('koniec')
print('=========')

print()
print('Cwiczenie 8')
print()

# Wymagania dotyczące haseł do danego systemu logowania są następujące:
#
# długość hasła powyżej 10 znaków
# hasło zawiera minimum jeden znak '!'
# Korzystając z pętli, instrukcji warunkowej i instrukcji break zbuduj walidator hasła: 'jnhvsoics!vd'
#
# Wydrukuj do konsoli 'Hasło poprawne' lub 'Hasło niepoprawne' w zależności od pomyślności walidacji.

password = 'j!elfkvmneoend'
if len(password) > 10:
    for i in password:
        if '!' in password:
            print('Hasło poprawne')
            break
    else:
        print('Hasło niepoprawne')
else:
    print('Hasło niepoprawne')
