#  set comprehention

text = 'Python jest wspaniały. Python jest elastyczny. Python rządzi'
words = text.lower()
print(words)
words = text.lower().replace('.','').split()
print(words)

unique_words = {word for word in words}
print(unique_words)

unique_words_grt = {word for word in words if len(word) > 4}
print(unique_words_grt)

word_capitalize = {word.capitalize() if word.startswith('pyt') else word for word in words}
print(word_capitalize)


# Ćwiczenie 3
# Z podanego tekstu:
#
# text = 'python jest popularny w uczeniu maszynowym'
# Dzięki set comprehension stwórz zbiór zawierający unikalne znaki,
# a następnie wydrukuj liczbę unikalnych znaków w podanym tekście.

text_1 = 'python jest popularny w uczeniu maszynowym'

how_many_letters = {word for word in text_1}
print(len(how_many_letters))
