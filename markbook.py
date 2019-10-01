"""
Markbook Application
Group members: Aidan, Ryan, Henson, Eric
"""
import pickle
import operator
from tkinter import *

all_courses = {}
all_students = {}

mainwin = Tk()
mainwin.geometry('1920x1080')
mainwin.title('Markbook')

firstnamelist = []
lastnamelist = []
numberlist = []

coursename = StringVar()
coursecode = StringVar()
courseperiod = StringVar()
courseteacher = StringVar()
studentnumber = StringVar()
assignmentname = StringVar()
ass_name = StringVar()
ass_due = StringVar()
ass_point = StringVar()
firstname = StringVar()
lastname = StringVar()


class course:  # class containing info related to the course
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

    def edit_assignement(self, ass_name):
        for assignment in self.assignment_list:
            if assignment.name == ass_name:
                while True:
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
        topwin = Toplevel()
        topwin.geometry('1920x1080')
        topwin.title('Add Assignment')
        frame1 = Frame(topwin)
        frame1.pack(fill=X)
        label_course = Label(frame1, text='Assignment Name:')
        label_course.pack(side=LEFT, padx=5, pady=5)
        entry_course = Entry(frame1, textvariable=ass_name)
        entry_course.pack(side=LEFT, fill=X, expand=True)
        frame2 = Frame(topwin)
        frame2.pack(fill=X)
        label_code = Label(frame2, text='Assignment Due Date:')
        label_code.pack(side=LEFT, padx=5, pady=5)
        entry_code = Entry(frame2, textvariable=ass_due)
        entry_code.pack(side=LEFT, fill=X, expand=True)
        frame3 = Frame(topwin)
        frame3.pack(fill=X)
        label_period = Label(frame3, text='Assignment Points:')
        label_period.pack(side=LEFT, padx=5, pady=5)
        entry_period = Entry(frame3, textvariable=ass_point)
        entry_period.pack(side=LEFT, fill=X, expand=True)
        frame4 = Frame(topwin)
        frame4.pack(fill=X)
        submit_button = Button(frame4, text='Submit',
                               command=lambda: [self.assignment_list.append(assignment(ass_name.get(),
                                                                                       ass_due.get(),
                                                                                       ass_point.get(),
                                                                                       self.code)), topwin.destroy()])
        submit_button.pack(side=TOP)

    def class_average(self):
        total = 0
        for stu in self.students_list:
            total += all_students[stu].get_average(self.code)
        average = total / len(self.students_list)
        return average


class student:  # class containing info about the student
    def __init__(self, first_name, last_name, stu_num):
        self.first = first_name
        self.last = last_name
        self.stu_num = stu_num
        self.course_list = []

    def add_course(self, new_course):
        if new_course.code not in self.course_list:
            self.course_list.append(new_course.code)
            new_course.students_list.append(self.stu_num)

    def get_average(self, code):
        mark = 0
        point = 0
        cou = all_courses[code]
        for ass in cou.assignment_list:
            mark += ass.marks[self.stu_num]
            point += ass.point
        average = mark / point
        return average


class assignment:  # class containing info about any assignments
    def __init__(self, name, due, point, course):
        self.name = name.capitalize()
        self.due = due
        self.point = point
        self.course = course
        self.marks = {}

    def mark_stu(self):
        stu = all_students[(int(input("student number: ")))]
        cou = all_courses[self.course]
        if stu.stu_num in cou.students_list:
            marks = int(input("marks: "))
            self.marks[stu.stu_num] = marks

    def print_mark(self):
        for num in self.marks:
            stu = all_students[num]
            print(stu.first, stu.last, stu.stu_num, self.marks[num])

    def average_mark(self):
        total = 0
        for mark in self.marks.values():
            total += mark
        average = ((total / len(self.marks)) / self.point) * 100
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
    topwin = Toplevel()
    topwin.geometry('1920x1080')
    topwin.title('Course Menu')
    create_a_course = Button(topwin, command=create_course, text='Create a course')
    create_a_course.pack(side=TOP, padx=5, pady=5)
    edit_a_course = Button(topwin, command=edit_course_prior, text='Edit a course')
    edit_a_course.pack(side=TOP, padx=5, pady=5)
    all_courses = Button(topwin, command=show_all_course, text='Show all courses')
    all_courses.pack(side=TOP, padx=5, pady=5)
    detail_course = Button(topwin, command=show_course, text='Show course in detail')
    detail_course.pack(side=TOP, padx=5, pady=5)
    backbutton = Button(topwin, command=topwin.destroy, text='Go Back')
    backbutton.pack(side=TOP, padx=5, pady=5)
    # elif input_ == "b":
    # edit_course(all_courses[(input("code: ").upper())])
    # elif input_ == "d":
    # show_course(all_courses[(input("code: ").upper())])


def create_course():
    topwin = Toplevel()
    topwin.title('Create Course')
    topwin.geometry('1920x1080')
    frame1 = Frame(topwin)
    frame1.pack(fill=X)
    label_course = Label(frame1, text='Course Name:')
    label_course.pack(side=LEFT, padx=5, pady=5)
    entry_course = Entry(frame1, textvariable=coursename)
    entry_course.pack(side=LEFT, fill=X, expand=True)
    frame2 = Frame(topwin)
    frame2.pack(fill=X)
    label_code = Label(frame2, text='Course Code:')
    label_code.pack(side=LEFT, padx=5, pady=5)
    entry_code = Entry(frame2, textvariable=coursecode)
    entry_code.pack(side=LEFT, fill=X, expand=True)
    frame3 = Frame(topwin)
    frame3.pack(fill=X)
    label_period = Label(frame3, text='Course Period: ')
    label_period.pack(side=LEFT, padx=5, pady=5)
    entry_period = Entry(frame3, textvariable=courseperiod)
    entry_period.pack(side=LEFT, fill=X, expand=True)
    frame4 = Frame(topwin)
    frame4.pack(fill=X)
    label_teacher = Label(frame4, text='Course Teacher:')
    label_teacher.pack(side=LEFT, padx=5, pady=5)
    entry_period = Entry(frame4, textvariable=courseteacher)
    entry_period.pack(side=LEFT, fill=X, expand=True)
    frame5 = Frame(topwin)
    frame5.pack(fill=X)
    submit_button = Button(frame5, text='Submit', command=lambda: [create_course_confirm(), topwin.destroy()])
    submit_button.pack(side=TOP)


def create_course_confirm():
    if coursecode.get() not in all_courses.keys():
        cou = course(coursename.get(), coursecode.get(), courseperiod.get(), courseteacher.get())
        all_courses[coursecode.get()] = cou


def edit_course_prior():
    topwin = Toplevel()
    topwin.title('Enter Course Code')
    topwin.geometry('1920x1080')
    code_label = Label(topwin, text='Enter Course Code:')
    code_label.pack(side=LEFT, padx=5, pady=5)
    code_entry = Entry(topwin, textvariable=coursecode)
    code_entry.pack(side=LEFT, fill=X, expand=True)
    enterbutton = Button(topwin, text='Enter', command=lambda: [edit_course(get_value(all_courses,
                                                                (coursecode.get()).upper())), topwin.destroy()])
    enterbutton.pack(side=LEFT)


def edit_course(cou):
    topwin = Toplevel()
    topwin.title('Edit Course')
    topwin.geometry('1920x1080')
    assignment_button = Button(topwin, text='Add Assignment', command=cou.add_assignment)
    assignment_button.pack(side=TOP, padx=5, pady=5)
    student_button = Button(topwin, text='Add Student to Course', command=lambda: add_student_ass(cou))
    student_button.pack(side=TOP, padx=5, pady=5)
    remove_button = Button(topwin, text='Remove student from a course', command=lambda: remove_student_ass(cou))
    remove_button.pack(side=TOP, padx=5, pady=5)
    edit_button = Button(topwin, text='Edit assignment', command=lambda: edit_assignment_ass(cou))
    edit_button.pack(side=TOP, padx=5, pady=5)


def add_student_ass(cou):
    topwin = Toplevel()
    topwin.title('Add Student')
    topwin.geometry('1920x1080')
    code_label = Label(topwin, text='Enter Student Number:')
    code_label.pack(side=LEFT, padx=5, pady=5)
    code_entry = Entry(topwin, textvariable=studentnumber)
    code_entry.pack(side=LEFT, fill=X, expand=True)
    enterbutton = Button(topwin, text='Enter', command=lambda: [cou.add_student(all_students[int(studentnumber.get())]),
                                                                topwin.destroy()])
    enterbutton.pack(side=LEFT)


def remove_student_ass(cou):
    topwin = Toplevel()
    topwin.title('Remove Student')
    topwin.geometry('1920x1080')
    code_label = Label(topwin, text='Enter Student Number:')
    code_label.pack(side=LEFT, padx=5, pady=5)
    code_entry = Entry(topwin, textvariable=studentnumber)
    code_entry.pack(side=LEFT, fill=X, expand=True)
    enterbutton = Button(topwin, text='Enter',
                         command=lambda: [cou.remove_student(all_students[int(studentnumber.get())]), topwin.destroy()])
    enterbutton.pack(side=LEFT)


def edit_assignment_ass(cou):
    topwin = Toplevel()
    topwin.title('Remove Student')
    topwin.geometry('1920x1080')
    code_label = Label(topwin, text='Enter Assignment Name:')
    code_label.pack(side=LEFT, padx=5, pady=5)
    code_entry = Entry(topwin, textvariable=assignmentname)
    code_entry.pack(side=LEFT, fill=X, expand=True)
    enterbutton = Button(topwin, text='Enter', command=lambda: [cou.edit_assignement((assignmentname.get()).upper()),
                                                                topwin.destroy()])
    enterbutton.pack(side=LEFT)


def student_menu():
    topwin = Toplevel()
    topwin.geometry('1920x1080')
    topwin.title('Student Menu')
    add_a_student = Button(topwin, command=create_student, text='Add student')
    add_a_student.pack(side=TOP, padx=5, pady=5)
    del_a_student = Button(topwin, command=remove_student, text='Delete a Student')
    del_a_student.pack(side=TOP, padx=5, pady=5)
    list_students = Button(topwin, command=show_all_student, text='List all students')
    list_students.pack(side=TOP, padx=5, pady=5)
    show_a_student = Button(topwin, command=show_student, text='Show a student in detail')
    show_a_student.pack(side=TOP, padx=5, pady=5)
    edit_a_student = Button(topwin, command=edit_student_prior, text='Edit a student')
    edit_a_student.pack(side=TOP, padx=5, pady=5)
    backbutton = Button(topwin, command=topwin.destroy, text='Go Back')
    backbutton.pack(side=TOP, padx=5, pady=5)
    # elif input_ == "d":
    # show_student(all_students[(int(input("student number: ")))])
    # elif input_ == "e":
    # edit_student(all_students[(int(input("student number: ")))])


def edit_student_prior():
    topwin = Toplevel()
    topwin.title('Enter Student Number')
    topwin.geometry('1920x1080')
    code_label = Label(topwin, text='Enter Student Number:')
    code_label.pack(side=LEFT, padx=5, pady=5)
    code_entry = Entry(topwin, textvariable=studentnumber)
    code_entry.pack(side=LEFT, fill=X, expand=True)
    enterbutton = Button(topwin, text='Enter',
                         command=lambda: [edit_student(get_value(all_students, convert_int(studentnumber.get()))),
                                          topwin.destroy()])
    enterbutton.pack(side=LEFT)



def edit_student(stu):
    topwin = Toplevel()
    topwin.geometry('1920x1080')
    topwin.title('Edit Student')
    add_to_course = Button(topwin, command=lambda:add_student_to_course(stu), text='Add student to course')
    add_to_course.pack(side=TOP, padx=5, pady=5)


def add_student_to_course(stu):
    topwin = Toplevel()
    topwin.geometry('1920x1080')
    topwin.title('Edit Student')
    code_label = Label(topwin, text='Enter Course Code:')
    code_label.pack(side=LEFT, padx=5, pady=5)
    code_entry = Entry(topwin, textvariable=coursecode)
    code_entry.pack(side=LEFT, fill=X, expand=True)
    enterbutton = Button(topwin, text='Enter',
                         command=lambda: [stu.add_course(all_courses[coursecode.get()]), topwin.destroy()])
    enterbutton.pack(side=LEFT)

def create_student():
    topwin = Toplevel()
    topwin.geometry('1920x1080')
    topwin.title('Create Student')
    frame1 = Frame(topwin)
    frame1.pack(fill=X)
    label_course = Label(frame1, text='First Name:')
    label_course.pack(side=LEFT, padx=5, pady=5)
    entry_course = Entry(frame1, textvariable=firstname)
    entry_course.pack(side=LEFT, fill=X, expand=True)
    frame2 = Frame(topwin)
    frame2.pack(fill=X)
    label_code = Label(frame2, text='Last Name:')
    label_code.pack(side=LEFT, padx=5, pady=5)
    entry_code = Entry(frame2, textvariable=lastname)
    entry_code.pack(side=LEFT, fill=X, expand=True)
    frame3 = Frame(topwin)
    frame3.pack(fill=X)
    label_period = Label(frame3, text='Student Number: ')
    label_period.pack(side=LEFT, padx=5, pady=5)
    entry_period = Entry(frame3, textvariable=studentnumber)
    entry_period.pack(side=LEFT, fill=X, expand=True)
    frame5 = Frame(topwin)
    frame5.pack(fill=X)
    submit_button = Button(frame5, text='Submit', command=lambda: [create_student_confirm(), topwin.destroy()])
    submit_button.pack(side=TOP)


def create_student_confirm():
    if studentnumber.get() not in all_students.keys():
        new_student = student(firstname.get(), lastname.get(), studentnumber.get())
        all_students[studentnumber.get()] = new_student


def remove_student():
    topwin = Toplevel()
    topwin.geometry('1920x1080')
    topwin.title('Remove Student')
    code_label = Label(topwin, text='Enter Student Number:')
    code_label.pack(side=LEFT, padx=5, pady=5)
    code_entry = Entry(topwin, textvariable=studentnumber)
    code_entry.pack(side=LEFT, fill=X, expand=True)
    enterbutton = Button(topwin, text='Enter',
                         command=lambda: [remove_student_confirm(studentnumber.get()), topwin.destroy()])
    enterbutton.pack(side=LEFT)


def remove_student_confirm(stu):
    if stu in all_students.keys():
        del all_students[stu]


def show_all_student():
    topwin = Toplevel()
    topwin.geometry('1920x1080')
    topwin.title('List of Students')
    for stu in all_students.values():
        firstnamelist.append(stu.first)
        lastnamelist.append(stu.last)
        numberlist.append(stu.stu_num)
    frame = Frame(topwin)
    frame.pack(fill=Y)
    text = Text(frame)
    for name in firstnamelist:
        text.insert(END, name + '\n')
    text.pack(side=LEFT, padx=5, pady=5)
    frameone = Frame(topwin)
    frameone.pack(fill=Y)
    textone = Text(frameone)
    for name in lastnamelist:
        textone.insert(END, name + '\n')
    textone.pack(side=LEFT, padx=5, pady=5)
    texttwo = Text(topwin)                       # Some reason, this box doesn't want to show up, will check at school
    for num in numberlist:
        texttwo.insert(END, num + '\n')
    texttwo.pack(side=LEFT)
    topwin.mainloop()


def show_student(stu):
    if isinstance(stu, student):
        print(stu.first, stu.last, stu.stu_num)          # I tried, But I don't know how to put this into tkinter (My
        for code in stu.course_list:                     # brain hurts so I'm going to sleep)
            cou = all_courses[code]
            print(cou.name, stu.get_average(cou.code))


def show_all_course():
    for cou in all_courses.values():
        print(cou.name, cou.code, len(cou.students_list))


def show_course(cou):
    if isinstance(cou, course):
        print(cou.name, cou.code, cou.period, cou.teacher,
              cou.class_average())
        for num in cou.students_list:
            stu = all_students[num]
            print(stu.first, stu.last, stu.stu_num, stu.get_average(cou.code))


def mainwingui():
    studentbutton = Button(mainwin, command=student_menu, text='Manage Students')
    studentbutton.pack(side=TOP, padx=5, pady=5)
    coursebutton = Button(mainwin, command=course_menu, text='Manage Courses')
    coursebutton.pack(side=TOP, padx=5, pady=5)
    savebutton = Button(mainwin, text='Save All Changes', command=saveation)
    savebutton.pack(side=TOP, padx=5, pady=5)


def saveation():
    with open("markbooksave", "wb") as output:
        pickle.dump(all_students, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(all_courses, output, pickle.HIGHEST_PROTOCOL)


def main():
    global all_students, all_courses
    with open("markbooksave", "rb") as input_:
        all_students = pickle.load(input_)
        all_courses = pickle.load(input_)
    mainwingui()
    mainwin.mainloop()


if __name__ == "__main__":
    main()
