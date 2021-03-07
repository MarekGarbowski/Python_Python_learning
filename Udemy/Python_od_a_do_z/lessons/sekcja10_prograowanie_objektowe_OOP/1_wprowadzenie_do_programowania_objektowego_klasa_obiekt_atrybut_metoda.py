class Tree:

    name = 'sosna'
    age = 40
    height = 25


tree_1 = Tree()
tree_2 = Tree()
print(id(tree_1))
print(id(tree_2))
print(tree_1.name)
print(tree_1.height)
print(tree_1.age)

print(tree_2.name)
print(tree_2.height)
print(tree_2.age)

tree_1.state = 'good'
print(dir(tree_1))

Tree.place = 'forest'
print(dir(Tree))
print(dir(tree_1))
print(dir(tree_2))

tree_2.place = 'park'
print(tree_2.place)
print(Tree.place)
