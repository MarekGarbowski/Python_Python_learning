import  pandas

techs = ['python', 'java', 'sql', 'r', 'scala']

with open('data.txt', 'w') as file:
    for tech in techs:
        print(tech, file=file)
print('1=====')

even_number = list(range(100))[::2]

with open('data.txt', 'w') as file:
    for number in even_number:
        file.write(str(number))

print('2=====')

even_number = list(range(100))[::2]

with open('data.txt', 'a') as file:
    for number in even_number:
        file.write(str(number) + '\n')
print('3=====')

techs = ['python', 'java', 'sql', 'r', 'scala']

with open('data.txt', 'a') as file:
    for tech in techs:
        print(tech, file=file)
print('4=====')

technologies = []

with open('data.txt', 'r') as file:
    for line in file:
        technologies.append(line[:-1])
print(technologies)
print('==========')
print()


print('Cwiczenie 3')
print()

# Utwórz listę z podanych nazw technologii:
#
# python
# java
# sql
# sas
# Następnie zapisz każdy element listy w nowej linii pliku techs.txt.

# techno = ['python', 'java', 'sql', 'sas']
#
# with open('techs.txt', 'w') as file:
#     for tech in techno:
#         file.write(tech + '\n')
#
# print('druga wersja tego samego:')
#
# with open('techs.txt', 'w') as file:
#     for tech in techno:
#         print(tech, file=file)


print('======')

with open('techs1.txt', 'w') as file:
    for j in range(2):
        for i in range(10):
            print('{:>9}'.format('*' * i), end='', file=file)
            print('{}'.format('*' * i), file=file)


