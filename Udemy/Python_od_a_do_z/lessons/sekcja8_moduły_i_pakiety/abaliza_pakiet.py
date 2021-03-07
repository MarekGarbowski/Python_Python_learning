
import rocket.data
import rocket.algorytmy
from rocket.algorytmy import drzewa_decyzyjne
from rocket.funkcje.stats import mean


print(dir(rocket.data))
print(dir(rocket.algorytmy))

dane = rocket.data.get_data()
print(dane)


algor = rocket.algorytmy.drzewa_decyzyjne()
print(algor)


drzewa_decyzyjne()
print(mean(dane))
