#-*- coding: utf-8 -*-

MAP_STUDENTS = {}


def show_all():
    list_stud = sorted(MAP_STUDENTS)
    for name in list_stud:
        print("*********************************")
        print(f"Subject for {name}:")
        for i, sub in enumerate(MAP_STUDENTS[name]):
            print(f"{i}. {sub}")

        print("*********************************")


def student_for_sub(student):
    return MAP_STUDENTS[student]


def sub_for_student(subject):
    list_student = []
    for k in MAP_STUDENTS:
        if subject in MAP_STUDENTS[k]:
            list_student.append(k)
    return list_student

if __name__ == '__main__':
    number_of_students = int(input("Please, enter count students: "))

    for i in range(number_of_students):
        name = input("Enter name student: ")
        subjects = input("Enter subjects (separated by space): ")
        if name not in MAP_STUDENTS:
            MAP_STUDENTS[name] = subjects.split(" ")

    print(student_for_sub("Vasya"))
    print(sub_for_student("math"))
    show_all()
