
class Human:

    pochodzenie = 'Ziemia'
    imie = 'Jack'


class Polak:

    kraj = 'Polska'
    imie = 'Piotr'


class Piłkarz(Human, Polak):

    def info(self):
        print(f'Utworzony obiekt pochodzi z planety {self.pochodzenie}.\nKraj pochodzenie {self.kraj}.'
              f'Nazwa obiektu {self.imie}')


pilkarz_1 = Piłkarz()
pilkarz_1.info()
