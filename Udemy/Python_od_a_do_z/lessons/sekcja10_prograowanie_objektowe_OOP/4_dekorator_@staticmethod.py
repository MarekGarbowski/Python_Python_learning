class Student:
    student_list = []

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.student_list.append(self)

    @staticmethod  # dekorator staticmethod jest używany poza klasą
    def number_of_students():
        print('Liczba studentów: ', len(Student.student_list))  # aby użyc tego dekoratora należy
        # odwołać się do nazwy klasy


student_1 = Student('Jan', 'Kowalski', 18)
student_2 = Student('Marek', 'Nowak', 23)
student_3 = Student('Arek', 'Nowak', 28)
student_4 = Student('Jan', 'Nowak', 32)

Student.number_of_students()
