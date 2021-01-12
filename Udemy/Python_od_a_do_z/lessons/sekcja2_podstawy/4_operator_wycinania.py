
# name[start:stop]
# name[:stop]
# name[start:]
# name[start:stop:step]
# Indeksacja jest podawana w nawiasach kwadratowych
# Indeksacja na liczbach dodatnich zaczyna się od "0" i jest liczona od lewej strony
# Indeksacja na liczbach ujemnych zaczyna się od "-1" i jest liczona od prawej strony

name = 'Python'
print(name)
print(name[0])
print(name[2:])
print(name[-1])
print(name[-2:])
print(name[1:4])
print(name[:])

full = 'Python programming'
print(full[7:])
print(full[-11:])
print(full[::2]) # wycięcie z napisu co drugiej wartości
print(full[::3]) # wycięcie z napisu co trzeciej wartości

sample = '#stop#this#flow'
print(sample[::5])

numbers = '8,9,4,2'
print(numbers[::2])

print(numbers[::-1])
print(numbers[::-2])

print('s' in sample)
print('S' in sample)

# Cwiczenie 4
# Podany jest tekst: "09023-Python-32"
#
# Wydrukuj numer indeksu startowego i indeksu końcowego pozwalającego wyciąć słowo 'Python'
# oddzielonego tylko przecinkiem, np. print('3,4').

name1 = '09023-Python-32'
print(name1[6:12])
print(name1[-9:-3])
print(name1[6:-3])
print(name1[-9:12])
print('6,12')

