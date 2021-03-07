class Human:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def info(self):
        print(f'{self.name} {self.surname}')


class Player(Human):
    def __init__(self, name, surname, team_name):
        super().__init__(name, surname)
        self.team_name = team_name

    def player_info(self):
        super().info()
        print(f'Klub: {self.team_name}')


player_1 = Player('Marek', 'Garbowski', 'Benfica')
player_2 = Player('Adam', 'Słodowy', 'Kracovia')


# player_1.info()
# player_2.info()
player_1.player_info()
player_2.player_info()
