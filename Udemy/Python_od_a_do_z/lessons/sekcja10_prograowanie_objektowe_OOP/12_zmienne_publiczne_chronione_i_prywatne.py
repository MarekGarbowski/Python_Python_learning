
# zmienna public: zmienna - dostępna z poziomu klasy, klasy pochodnej i wszędzie poza klasą pochodną
# zmienna protected: _zmienna - dostępna z poziomu klasy i tylko z poziomu klasy pochodnej
# zmienna private: __zmienna - dostępna tylko z poziomu klasy ktre konfinikujemy

class Spolka:

    def __init__(self, rodzaj, rynek, gielda):
        self.rodzaj = rodzaj
        self._rynek = rynek
        self.__gielda = gielda


class KGHM(Spolka):

    def __init__(self, rodzaj, rynek, gielda, nazwa):
        super().__init__(rodzaj, rynek, gielda)
        self.nazwa = nazwa
        print(f'Atrybut publiczny: {self.rodzaj}')
        print(f'Atrybut chroniony: {self._rynek}')
        # print(f'Atrybut prywatny: {self.__gielda}')


spolka = Spolka('Spółka Akcyjna', 'Główny', 'GPW w Warszawie')
print(f'Atrybut publiczny: {spolka.rodzaj}')
print(f'Atrybut chroniony {spolka._rynek}')
# print(f'Atrybut prywatny {spolka.__gielda}')


kghm = KGHM('Spółka Akcyjna', 'Główny', 'GPW w Warszawie', 'KGHM')
