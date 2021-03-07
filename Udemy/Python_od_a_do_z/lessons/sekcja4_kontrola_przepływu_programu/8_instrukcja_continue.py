for i in range(10):
    if i == 6:
        continue
    print(i)
print('=====')

for i in range(20):
    if i % 2 == 0:
        continue
    print(i)
print('=====')

sample = 'python course'
for char in sample:
    if char == ' ':
        continue
    print(char)
print('=====')


hashtags = '#summer#holiday#free'
result = ''
for l in hashtags:
    if l == '#':
        print(result)
        result = ""
        continue
    result += l
print(result)

print('=========')
print()

print('Cwiczenie 9')
print('')

# Podana jest lista:
#
# lista = [1, 2, 99, 4, 5]
# Wydrukuj wszystkie cyfry do konsoli używając pętli for, pomiń wartość 99 (każda cyfra w osobnej linii)
#
# Wskazówka: Skorzystaj z instrukcji continue

lista = [1, 2, 99, 4, 5]
for l in lista:
    if l == 99:
        continue
    print(l)
