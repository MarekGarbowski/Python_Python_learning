for i in 'python':
    print(i)
print('=====')
print()

indexx = 0
for e in 'windows':
    print(indexx, e)
    indexx += 1
print('=====')

for q in range(10):
    print(q)
print('=====')
name = 'python'
for a in range(len(name)):
    print(a)
print('=====')
print('=====')
name = 'python'
for a in range(len(name)):
    print('numer indeksu: ', a, 'litera: ', name[a])
print('=====')

for enu in enumerate(name):
    print(enu)

for index, value in enumerate(name):
    print(index, value)
print('=====')

for i in [1, 2, 3, 4, 5]:
    print(i)
print('=====')

for i, v in enumerate([1, 2, 3, 4, 5]):
    print(i, v)
print('======')

for d in range(10):
    print(d)
print('=====')

for i in range(10, 20):
    print(i)
print('=====')

for i in range(1, 20, 2):
    print(i)
print('=====')

for i in range(10, -1, -1):
    print(i)
print('=====')

techs = 'java'
for i in range(len(techs)):
    print(i, techs[i])
print('=====')

string = 'python course'
for char in string:
    print(char)
print('=====')

string = 'python course'
for char in string[:6]:
    print(char)
print('=====')

string = 'python course'
for char in string[::2]:
    print(char)
print('=====')

string = 'python course'
for char in string[::-1]:
    print(char)
print('=====')

hashtag = '#sport#gym#fitness'
for char in hashtag:
    print(char)
print('=====')

hashtag = '#sport#gym#fitness'
for char in hashtag:
    if char != '#':
        print(char)
print('=====')

for chr in zip('abcde', '123456'):
    print(chr)
print('=====')

for chr, num in zip('abcde', '12345678'):
    print(chr, num)
print('=====')

result = ''
for znak in hashtag:
    print(znak)
print('=====')

result = ''
for znak in hashtag:
    if znak not in '#':
        result = result + znak
    else:
        print(result)
        result = ''
print('==========')
print()

print('Cwiczenie 6')

# Korzystając z pętli wydrukuj do konsoli liczby od 0 do 20 włącznie.
#
# Uwaga: Każda liczba w osobnej linii!

for digit in range(21):
    print(digit)

print('=====')
print()

print('Cwiczenie 7')

# Podany jest ciąg znaków:
#
# '#weekend#good#time#'
# Zbuduj skrypt, który wydrukuje do konsoli wyciągnięte z tego tekstu słowa. Każde słowo w nowej linii.
#
# Wskazówka: Należy skorzystać z pętli a także z instrukcji warunkowej.

x = '#weekend#good#time#'
words = ''
for letter in x:
    if letter != '#':
        words += letter  # można też: words = words + letter
    else:
        print(words)
        words = ''
