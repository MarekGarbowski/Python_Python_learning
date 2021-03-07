
results = []

for i in range(100):
    results.append(i**2)
print(results)


print()
print('*' * 30)
print()

#  drugi sposób

results_2 = [ii ** 2 for ii in range(100)]
print(results_2)

print()
print('*' * 30)
print()

# dalsza rozbudowa o kolejne instrukcje

wyniki = []

for a in range(100):
    if a % 5 == 0:
        wyniki.append(a ** 2)
print(wyniki)

# to samo tylko w list comprehension

wyniki1 = [a ** 2 for a in range(100) if a % 5 == 0]
print(wyniki1)

print()
print('*' * 30)
print()

letters = ['a', 'b', 'c']
numbers = ['1', '2', '3']

result = []
for letter in letters:
    for number in numbers:
        result.append(letter + number)
print(result)

# to samo z list comprehension

results_2 = [letter + number for letter in letters for number in numbers]
print(results_2)

print()
print('*' * 30)
print()

letters_1 = ['a', 'b', 'c']
letters_2 = ['a', 'b', 'c']
result_3 = [letter_1 + letter_2 for letter_1 in letters_1 for letter_2 in letters_2]
result_4 = [letter_1 + letter_2 for letter_1 in letters_1 for letter_2 in letters_2 if letter_1 != letter_2]
print(result_3)
print(result_4)

print()
print('*' * 30)
print()

# generowanie danych dzięki list comprehension

q = [[j for j in range(1, 11)] for i in range(2)]
print(q)

qq = [[(ii, jj) for jj in range(10)] for ii in range(3)]
print(qq)

qqq = [[iii * jjj for jjj in range(10)] for iii in range(3)]
print(qqq)

print()
print('*' * 30)
print()

# list comprehension z danymi tekstowymi

list_1 = [l1 for l1 in '12345']
print(list_1)

list_2 = [[l1 + l2 for l2 in 'abcde'] for l1 in '12345']
print(list_2)

print()
print('*' * 30)
print()

# list comprehension w funkcji Silnia


def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)


nn = [silnia(i) for i in range(7)]
print(nn)


print()
print('*' * 30)
print()


# Ćwiczenie 1
# Używając list comprehension wydrukuj do konsoli listę liczba od zera do 30 podzielnych przez 4.
#
# Uwaga: Zadanie można zrobić przy pomocy jednej linii kodu.

numbers_1 = [number for number in range(30) if number % 4 == 0]
print(numbers_1)
