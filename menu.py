from markbook import *
import json


# Student Options
def student():

    while True:

        print("""
        Student OPTIONS
        1: Add
        2: Delete
        3: Edit
        4: Return to menu
        """)

        ask = int(input("What you you like to do: "))

        if ask == 1:
            print(add_student_to_classroom(student=input("Enter Student Name (last name, first name):")))

        elif ask == 2:
            print(remove_student_from_classroom(course_code=input("What course is the Student in: "),
                                                student=input("Enter Student Name (last name, first name):")))

        elif ask == 3:
            print(edit_student(course_code=input("What course is the Student in: "),
                               student=input("Enter Student Name (last name, first name):")))

        elif ask == 4:
            break
        else:
            print("Not a valid response. Please try again.")
            continue
    menu()


# Course options
def classroom():

    while True:

        print("""
        Course OPTIONS
        1: Create
        2: Delete
        3: Edit
        4: Return to menu
        """)

        ask = int(input("What you you like to do: "))

        if ask == 1:
            print(create_classroom(course_code=input("What is the course code:"),
                                   course_name=input("What is the course name:"),
                                   period=input("What period is the course in:"),
                                   teacher=input("Who is the teacher:")))
        elif ask == 2:
            delete_classroom(course_code=input("Please enter the course code to delete it:"))
        elif ask == 3:
            print(edit_classroom(course_code=input("Please enter the course code to edit it:")))
        elif ask == 4:
            break
        else:
            print("Not a valid response. Please try again.")
            continue

    menu()


# Assignment Option
def assignment():

    while True:

        print("""
        Assignment OPTIONS
        1: Create
        2: Delete
        3: Edit
        4: Return to menu
        """)

        ask = int(input("What you you like to do: "))

        if ask == 1:
            print(create_assignment(course_code=input("Enter the Course Code for the assignment: ")))
        elif ask == 2:
            print(delete_assignment(course_code=input("Enter the Course Code for the assignment: ")))
        elif ask == 3:
            print(edit_assignment(course_code=input("Enter the Course Code for the assignment: ")))
        elif ask == 4:
            break
        else:
            print("Not a valid response. Please try again.")
            continue

    menu()


# Markbook View Option
def markbook():

    while True:

        print("""
        Markbook OPTIONS
        1: View Markbook
        2: View Course Average
        3: Return to menu
        """)

        ask = int(input("What you you like to do: "))

        if ask == 1:
            with open("classroom.json", "r") as f:
                markbook = json.load(f)
            # prints out each course out with line skip
            for key, value in markbook.items():
                print("""
                {}:{}
                """.format(key, value))
        elif ask == 2:
            print (calculate_average_mark(course_code=input("Enter Course Code: ")))
        elif ask == 3:
            break
        else:
            print("Not a valid response. Please try again.")

    menu()


# Menu function, lets users navigate through the markbook.
def menu():

    print ("""
        Welcome to Markbook
        1: Student
        2: Classroom
        3: Assignments
        4: Markbook
        5: Quit
    """)

    ask = int(input("What would you like do: "))

    if ask == 1:
        student()

    elif ask == 2:
        classroom()

    elif ask == 3:
        assignment()

    elif ask == 4:
        markbook()

    elif ask == 5:
        q = input("Are you sure you want to quit (y/n):")

        if q == "y":
            quit()
        else:
            menu()

menu()
