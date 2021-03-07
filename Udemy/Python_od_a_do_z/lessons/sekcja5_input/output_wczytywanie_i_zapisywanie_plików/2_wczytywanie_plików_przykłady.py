
with open('simple.txt', 'r') as file:
    line = file.readline()
    print(line)
print('1======')

with open('simple.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
print('2======')

with open('simple.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
print('3======')

with open('simple.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()
print('4======')

with open('simple.txt', 'r') as file:
    line = file.read()
    print(line)
print('5======')
print()
print('=========')
print()

print('Cwiczenie 2')
print()

# Wczytaj plik data.txt przy użyciu metody readlines(). Rezultat (listę) wydrukuj do konsoli.

with open('data.txt', 'r') as file:
    line1 = file.readlines()
    for line in line1:
        print(line, end='')
