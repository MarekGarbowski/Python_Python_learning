
class Student:

    student_list = []

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.student_list.append(self)

    @classmethod #  dekorator classmethod może być tylko używany w danej klasie
    def number_of_students(cls): #  wymagane słówko cls jako parametr funkcji
        print('Liczba studentów: ', len(Student.student_list))


student_1 = Student('Jan', 'Kowalski', 18)
student_2 = Student('Marek', 'Nowak', 23)
student_3 = Student('Arek', 'Nowak', 28)
student_4 = Student('Jan', 'Nowak', 32)

Student.number_of_students()