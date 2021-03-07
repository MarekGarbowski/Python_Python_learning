

class Tree:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def are_tree_protected(self):
        if self.age >= 20 and self.height >= 20:
            print(f'Drzewo o nazwie: "{self.name}" jest chronione.')
        else:
            print(f'Drzewo o nazwie: "{self.name}" nie jest chronione')

    def age_for_a_year(self):
        self.age += 1


tree_1 = Tree('sosna', 30, 25)
tree_2 = Tree('brzoza', 15, 18)
print(tree_1.name)
print(tree_2.name)
tree_1.are_tree_protected()
tree_2.are_tree_protected()
print(tree_1.age)
tree_1.age_for_a_year()
print(tree_1.age)
