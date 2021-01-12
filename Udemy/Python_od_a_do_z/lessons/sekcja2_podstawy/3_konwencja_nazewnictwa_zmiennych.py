
name = 'Marek'
_name = 'Tomek' # można używać ale tego typu na pisane zmienne są zarezerwowane dla zmiennych wewnętrznych Pythona
print(name, _name)
# 3marek = "Artur" niepoprwnie napisana nazwa zmiennej,nie mozna zaczynać od cyfr
marek3 = "Marek"
marek_3 = 'Marek'

# Opisywanie zmiennych upraszcza czytanie i analizę już napisanego programu
work_hours = 12
work_days = 4
total_work_time = work_days * work_hours
print(total_work_time)

# Style pisania w Pythonie

camelCase = 1
PascalCase = 2
snake_case = 3
# kebab-case = 4
UPPER = 5

# Domyślny styl: snake_case a do stałych tyl UPPER
import keyword
print(keyword.kwlist)
