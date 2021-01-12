
text = 'Witaj na kursie Pythona.\nPython jest super!'
print(text)
print(dir(text))
# print(help(str.count))

text = text.capitalize()
print(text)

text = text.title()
print(text)

text = text.count('Python')
print(text)

# test = text.startwith('Wi')
# print(str(test))

# print(text.find('Python'))

hashtags = 'sport#gym'
idx = hashtags.find('#')
hashtags = hashtags[:idx]
print(hashtags)

ally = 'pawel12!'
print(ally.isalnum())

qwe = '986'
print(qwe.isdigit())

name12 = 'kevnco'
print(name12.islower())

print(name12.isupper())

name123 = ' test '
print(name123.join(['Python', '333']))

text1 = '  #good#time#mood  '
print(text1.replace('#', ' '))
print(text1.strip())
print(text1.rstrip())
print(text1.lstrip())

asd = '1,2,3,4,5'
print(asd)
print(type(asd))
print(asd.split(','))
print(type(asd.split(',')))
print(asd)
print(type(asd))
print(text1.split('#'))

user = '12'
print(user.zfill(6))

# Ćwiczenie 6
# Używając odpowiedniej metody połącz podane wyrazy symbolem '#':
#
# sport
# python
# free
# time
# Następnie wydrukuj do konsoli.

gym = 'sport python free time'
print(gym.replace(" ", "#"))

result = '#'.join(['sport', 'python', 'free', 'time'])
print(result)

# Ćwiczenie 7
# Mamy podaną zmienną tekstową:
#
# x = '123,785,45,5'
# Używając odpowiedniej metody wyodrębnij dane liczbowe ze zmiennej x,
# tak aby rezultatem była lista wartości tekstowych zawierających same cyfry.
# Wynik wydrukuj do konsoli używając funkcji print().
#
# Oczekiwany rezultat:
#
# ['123', '785', '45', '5']

x = '123,785,45,5'
print(x.split(','))

print(13 //3)
