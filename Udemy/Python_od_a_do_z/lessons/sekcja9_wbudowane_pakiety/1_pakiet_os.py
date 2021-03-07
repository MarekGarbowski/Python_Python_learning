import os
print(os.getcwd())
# os.chdir('..') #  zmiana katalogu roboczego
# print(os.getcwd()) #  wyświetlenie katalogu aktualnego gdzie jesteśmy
# os.system('mkdir dir1') #  stworzenie katalogu w aktualnym folderze
# os.rmdir('dir1') #  usuni ecie katalogu

print(os.listdir()) #  wyświetlanie zawartośni katalogu

# listowanie w pythonie zawartości katlaogu
for item in os.listdir():
    print(item)
print()
print('*' * 30)
print()

# filtrowanie zawartości katalogu po rozszeżeniu

for item_1 in os.listdir():
    if item_1.endswith('.py'):
        print(item_1)

print()
print('*' * 30)
print()

for root, dirs, files in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    print(files)
print()
print('*' * 30)
print()
