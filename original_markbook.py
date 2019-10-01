"""
Markbook Application
Group members: Aidan, Ryan, Henson, Eric

"""
import pickle
import operator

all_courses = {}
all_students = {}


class course:
    def __init__(self, name, code, period, teacher):
        self.name = name
        self.code = code
        self.period = period
        self.teacher = teacher
        self.students_list = []
        self.assignment_list = []

    def add_student(self, new_student):
        if isinstance(new_student, student):
            if new_student.stu_num not in self.students_list:
                self.students_list.append(new_student.stu_num)
                new_student.course_list.append(self.code)

    def remove_student(self, stu):
        if isinstance(stu, student):
            if stu.stu_num in self.students_list:
                self.students_list.remove(stu.stu_num)
                stu.course_list.remove(self.code)

    def edit_assignment(self, ass_name):
        for assignment in self.assignment_list:
            if assignment.name == ass_name:
                while True:
                    print("Input nothing to go back\n"
                          "Input 'a' to enter a student mark\n"
                          "Input 'b' to print all marks"
                          "Input 'c' to print average mark")
                    input_ = input()
                    if input_ == "":
                        break
                    elif input_ == "a":
                        assignment.mark_stu()
                    elif input_ == "b":
                        assignment.print_mark()
                    elif input_ == "c":
                        print(assignment.average_mark())

    def add_assignment(self):
        ass_name = input("Name: ")
        ass_due = input("Due: ")
        ass_point = convert_int(input("Points: "))
        self.assignment_list.append(assignment(ass_name, ass_due,
                                    ass_point, self.code))

    def class_average(self):
        total = 0
        for stu in self.students_list:
            total += all_students[stu].get_average(self.code)
        average = total/len(self.students_list)
        return average


class student:
    def __init__(self, first_name, last_name, stu_num):
        self.first = first_name
        self.last = last_name
        self.stu_num = stu_num
        self.course_list = []

    def add_course(self, new_course):
        if new_course.code not in self.course_list:
            self.course_list.append(new_course.code)
            new_course.students_list.append(self.stu_num)

    def rm_course(self, old_course):
        if old_course.code in self.course_list:
            self.course_list.remove(old_course.code)
            old_course.students_list.remove(self.stu_num)

    def get_average(self, code):
        mark = 0
        point = 0
        cou = all_courses[code]
        for ass in cou.assignment_list:
            mark += ass.marks[self.stu_num]
            point += ass.point
        average = mark/point
        return average


class assignment:
    def __init__(self, name, due, point, course):
        self.name = name.upper()
        self.due = due
        self.point = point
        self.course = course
        self.marks = {}

    def mark_stu(self):
        stu = get_value(all_students, (convert_int(input("student number: "))))
        cou = all_courses[self.course]
        if stu.stu_num in cou.students_list:
            marks = convert_int(input("marks: "))
            self.marks[stu.stu_num] = marks

    def print_mark(self):
        for num in self.marks:
            stu = all_students[num]
            print(stu.first, stu.last, stu.stu_num, self.marks[num])

    def average_mark(self):
        total = 0
        for mark in self.marks.values():
            total += mark
        average = ((total/len(self.marks))/self.point)*100
        return average


def convert_int(num_true):
    try:
        val = int(num_true)
    except ValueError:
        val = convert_int(input("Not a num, enter a number: "))
        return val
    else:
        return val


def get_value(dict, key):
    try:
        value = dict[key]
    except KeyError:
        print(f"Error 404, key {key} not found")
    else:
        return value


def course_menu():
    while True:
        print("Input nothing to go back\nInput 'a' to create a new course\n"
              "Input 'b' to edit existing courses\n"
              "Input 'c' to print all courses\n"
              "Input 'd' to print course details")
        input_ = input()
        if input_ == "":
            break
        elif input_ == "a":
            create_course()
        elif input_ == "b":
            edit_course(get_value(all_courses, input("code: ").upper()))
        elif input_ == "c":
            print_all_course()
        elif input_ == "d":
            print_course(get_value(all_courses, input("code: ").upper()))


def create_course():
    name = input("course name: ")
    code = input("course code: ").upper()
    period = input("period: ")
    teacher = input("teacher: ")
    if code not in all_courses.keys():
        cou = course(name, code, period, teacher)
        all_courses[code] = cou


def edit_course(cou):
    if isinstance(cou, course):
        while True:
            print("Input nothing to go back\nInput 'a' to add assignment \n"
                  "Input 'b' to add student \n"
                  "Input 'c' to remove student \nInput 'd' to edit assignment")
            input_ = input()
            if input_ == "":
                break
            elif input_ == "a":
                cou.add_assignment()
            elif input_ == "b":
                cou.add_student(get_value(all_students, (convert_int(input(
                    "student_num: ")))))
            elif input_ == "c":
                cou.remove_student(all_students[(convert_int(input(
                    "student_num: ")))])
            elif input_ == "d":
                cou.edit_assignment(input("assignment name: ").upper())


def student_menu():
    while True:
        print("Input nothing to go back\nInput 'a' to add a student\n"
              "Input 'b' to remove students\n"
              "Input 'c' to show the student list\n"
              "Input 'd' to show student details\nInput 'e' to edit a student")
        input_ = input()
        if input_ == "":
            break
        elif input_ == "a":
            create_student()
        elif input_ == "b":
            remove_student(convert_int(input("student number: ")))
        elif input_ == "c":
            print_all_student()
        elif input_ == "d":
            print_student(get_value(all_students, convert_int(input(
                "student number: "))))
        elif input_ == "e":
            edit_student(get_value(all_students, (convert_int(input(
                "student number: ")))))


def edit_student(stu):
    if isinstance(stu, student):
        while True:
            print("Input nothing to go back \nInput 'a' to add course")
            input_ = input()
            if input_ == "":
                break
            elif input_ == "a":
                stu.add_course(get_value(all_courses, input("code: ").upper()))
            elif input_ == "b":
                stu.rm_course(get_value(all_course, input("code: ").upper()))


def create_student():
    print("Creating new student")
    first_name = input("first name: ")
    last_name = input("last name: ")
    stu_num = convert_int(input("student number: "))
    if stu_num not in all_students.keys() and type(stu_num) == int:
        new_student = student(first_name, last_name, stu_num)
        all_students[stu_num] = new_student


def remove_student(stu):
    if stu in all_students.keys():
        del all_students[stu]


def print_all_student():
    for stu in all_students.values():
        print(stu.first, stu.last, stu.stu_num)


def print_student(stu):
    if isinstance(stu, student):
        print(stu.first, stu.last, stu.stu_num)
        for code in stu.course_list:
            cou = all_courses[code]
            print(cou.name, stu.get_average(cou.code))


def print_all_course():
    for cou in all_courses.values():
        print(cou.name, cou.code, len(cou.students_list))


def print_course(cou):
    if isinstance(cou, course):
        print(cou.name, cou.code, cou.period, cou.teacher,
              cou.class_average())
        for num in cou.students_list:
            stu = all_students[num]
            print(stu.first, stu.last, stu.stu_num, stu.get_average(cou.code))


def main():
    global all_students, all_courses
    with open("markbooksave", "rb") as input_:
                all_students = pickle.load(input_)
                all_courses = pickle.load(input_)
    while True:
        print("Input 'a' to manage students\nInput 'b' to manage courses\n"
              "Input 's' to save")
        input_ = input()
        if input_ == "a":
            student_menu()
        elif input_ == "b":
            course_menu()
        elif input_ == "s":
            with open("markbooksave", "wb") as output:
                pickle.dump(all_students, output, pickle.HIGHEST_PROTOCOL)
                pickle.dump(all_courses, output, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main()
