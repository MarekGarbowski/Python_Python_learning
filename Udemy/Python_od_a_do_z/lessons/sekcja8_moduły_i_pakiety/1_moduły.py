# import rocket_science -- funkcja "from importuje wszystkie informacje z danego pliku
# funkcja from file import funkcja importuje tylko té konkretná funkcjé z danego pliku

from rocket_science import calculate_mean
from rocket_science import calculate_max
from rocket_science import calculate_min
from rocket_science import calculate_max, calculate_min

# print(dir(rocket_science))

print(calculate_mean([3, 4]))

print(calculate_max([3, 4]))

print(calculate_min([3, 4]))
