
def generator():

    yield 4
    yield 5


generator()

gen = generator()
print(next(gen))

print()
print('*' * 30)
print()


def generator_2(word):
    letters = list(word)
    for letter in letters:
        yield letter


gen_2 = generator_2('Python')

print(next(gen_2))

print()
print('*' * 30)
print()

for item in generator_2('Python'):
    print(item)

print()
print('*' * 30)
print()

files = ['script_1.py', 'script_2.py','text.txt']


# filtrowanie listy plików po na przykład rozszeżeniu pliku
def gen_files(lista):
    for item in lista:
        if item.endswith('.py'):
            yield item


gener = gen_files(files)
print(list(gener))

for i in gener:
    print(i)

print()
print('*' * 30)
print()

# Ćwiczenie 7
# Dana jest lista zawierająca nazwy plików w pewnym katalogu:
#
# files = ['run_me.py', 'README.md', 'help.txt.', 'script.py', 'menu.py', 'main.py', 'py']
# Stwórz generator o nazwie generator_py który przefiltruje podane nawy i zwróci tylko nazwy plików z rozszerzeniem '.py'.
#
# Uwaga: Wystarczy zdefiniować sam generator.

files1 = ['run_me.py', 'README.md', 'help.txt.', 'script.py', 'menu.py', 'main.py', 'py']


def generator_py(files2):
    for qw in files2:
        if qw.endswith('.py'):
            yield qw


file = generator_py(files1)
print(list(file))

