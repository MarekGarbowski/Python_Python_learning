
print(int.__add__(1, 2))

print(int.__sub__(11, 3))

'''
Operatory:

    + : __add__(self, other)
    - ; __sub__(self, other)
    * : __mul__(self, other)
    / : __trudiv__(self, other)
    // : __floordiv__(self, other)
    % : __mod__(self, other)
    ** : __pow__(self, other)

Operatory porównawcze:

    <  : __lt__(self, other)
    >  : __gt__(self, other)
    <= : __le__(self, other)
    >= : __ge__(self, other)
    == : __eq__(self, other)
    !  : __ne__(self, other)
    

'''

print(int.__lt__(3, 5))
print(int.__lt__(3, 2))


class SpecialInt(int):

    def __init__(self, special_int):
        self.special_int = special_int

    def __add__(self, other):
        return self.special_int + other.special_int


s_1 = SpecialInt(2)
s_2 = SpecialInt(3)
print(s_1 + s_2)


class Kwadrat:

    def __init__(self, dlugosc_boku):
        self.dlugosc_boku = dlugosc_boku

    def __str__(self):
        return f"Kwadrat o boku {self.dlugosc_boku} cm."

    def __add__(self, other):
        return self.dlugosc_boku ** 2 + other.dlugosc_boku ** 2

    def __sub__(self, other):
        return self.dlugosc_boku ** 2 - other.dlugosc_boku ** 2

    def __lt__(self, other):
        return self.dlugosc_boku ** 2 < other.dlugosc_boku ** 2

k1 = Kwadrat(3)
print(k1)
k2 = Kwadrat(10)
print(k2)

print(k1 + k2)
print(k2 - k1)
print(k1 < k2)

# Skrócenie kodu klasy:


class Kwadrat:

    def __init__(self, dlugosc_boku):
        self.dlugosc_boku = dlugosc_boku

    def __str__(self):
        return f"Kwadrat o boku {self.dlugosc_boku} cm."

    def pole(self):
        return self.dlugosc_boku ** 2  #  wydzielenie funkcji obliczania pola kwadratu do osobnej funkcji

    def __add__(self, other):
        return self.pole() + other.pole()

    def __sub__(self, other):
        return self.pole() - other.pole()

    def __lt__(self, other):
        return self.pole() < other.pole()


k3 = Kwadrat(5)
print(k3)
k4 = Kwadrat(8)
print(k4)

print(k3 + k4)
print(k4 - k3)
print(k3 < k4)
