
class A:

    def method(self):
        print('Metoda klasy A')


class B(A):

    def method(self):
        print('Metoda klasy B')


class C(A):

    def method(self):
        print('Metoda klasy C')


class D(B, C):

    pass

    def method(self):
        print('Metoda klasy D')


d = D()
d.method()
