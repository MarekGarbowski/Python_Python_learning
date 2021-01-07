# class Student:
#     # Konstruktor zostanie wywołany podczas tworzenia obiektu
#     def __init__(self):
#         print("powstaje nowy obiekt!")
#
#
# if __name__ == '__main__':
#     student = Student()

# class Student:
#     def __init__(self):
#         self.first_name = "Marek"
#         self.last_name = "Garbowski"
#         self.age = 43


# def run_example():
#     student = Student()
#     # Do stanu obiektu mamy dostęp - możemy do odczytać
#     # print(student.first_name)
#     # print(student.last_name)
#     # print(student.age)
#     student.first_name = "Tomasz"
#     student.last_name = "Kowalski"
#     student.age = 23
#     print(student.first_name)
#     print(student.last_name)
#     print(student.age)


# if __name__ == '__main__':
#     run_example()

# class Student:
#
#     # Konstruktor może przyjąć argumenty
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.promoted = False
#
# # Obiekty możemy przekazazywać jako argumenty do funkcji
#
#
# def print_student(student):
#     print(f"Student: {student.first_name} {student.last_name}, promoted: {student.promoted}")
#
#
# # W funkcji możemy zmodyfikować stan obiektu (side effect)
# def promote_student(student):
#     student.promoted = True
#
#
# def run_example():
#     student = Student(first_name="Adam", last_name="Słodowy")
#     print_student(student)
#
#     other_student = Student("Marek", "Długi")
#     print_student(other_student)
#
#     promote_student(student)
#     promote_student(other_student)
#     print_student(student)
#     print_student(other_student)


# if __name__ == '__main__':
#     run_example()


# import random
#
#
# # Obiekt moze zawierać w sobie inne obiekty
#
#
# class School:
#
#     def __init__(self, name, students):
#         self.name = name
#         self.students = students
#
#
# class Student:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.promoted = False
#
#
# def print_student(student):
#     print(f"Student: {student.first_name} {student.last_name}, promoted: {student.promoted}")
#
#
# def promote_student(student):
#     student.promote = True
#
#
# # Funkcja może zwracać obiekty
# def create_school_with_students(school_name):
#     number_of_students = random.randint(1, 20)
#     students = []
#     for student_number in range(number_of_students):
#         first_name = f"Student- {student_number}"
#         last_name = f"Kowalski"
#         # last_name = input("podaj nazwisko studenta")
#         students.append(Student(first_name, last_name))
#
#     school = School(school_name, students)
#     return school
#
#
# def run_example():
#     school = create_school_with_students("Hogwart")
#     print(school)
#     for student in school.students:
#         print_student(student)


# if __name__ == '__main__':
#     run_example()


# class School:
#
#     def __init__(self, name, students):
#         self.name = name
#         if len(students) > 10:
#             students = students[:10]
#         self.students = students
#
#
# class Student:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.promoted = False
#
#
# def print_student(student):
#     print(f"Student: {student.first_name} {student.last_name}, promoted: {student.promoted}")
#
#
# def create_school_with_students(school_name, number_of_students):
#     students = []
#     for student_number in range(number_of_students):
#         first_name = f"Student- {student_number}"
#         last_name = f"Kowalski"
#         # last_name = input("podaj nazwisko studenta")
#         students.append(Student(first_name, last_name))
#
#     school = School(school_name, students)
#     return school
#
#
# def run_example():
#     school = create_school_with_students("Hogwart", 40)
#     print(school)
#     for student in school.students:
#         print_student(student)
#
#
# if __name__ == '__main__':
#     run_example()


