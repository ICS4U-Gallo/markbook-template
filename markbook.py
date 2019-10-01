"""
Markbook Application
Group members: Marcus Tuen Muk, Liu Chen Wu, Stella Hong
"""
from typing import Dict
import json


def create_assignment(course_code: str) -> Dict:
    """Creates an assignment represented as a dictionary

    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    with open("assignment.json", "r") as f:
        assignment_List = json.load(f)

    name = input("What is the name of the assignment? ")
    due = input("When is the due date? ")
    points = int(input("How much is this assignment worth. "))

    assignment_List[course_code] = {
        name: {
            "name": name,
            "due": due,
            "points": points
        }
    }

    with open("assignment.json", "w") as f:
        json.dump(assignment_List, f)

    return assignment_List


def delete_assignment(course_code: str):
    to_be_deleted = input("Which assignment would you like to delete? ")

    with open("assignment.json", "r") as f:
        assignment_List = json.load(f)

    if assignment_List[course_code][to_be_deleted]["name"] == to_be_deleted:
        assignment_List.clear()

    with open("assignment.json", "w") as f:
        json.dump(assignment_List, f)

    return assignment_List


def edit_assignment(course_code: str):
    to_be_edited = input("Enter the assignment to be edited: ")

    with open("assignment.json", "r") as f:
        assignment_List = json.load(f)

    print("""
        Editing option
        1: Name
        2: Due Date
        3: Points
        """)

    # lets user choose what they want to change
    x = int(input("What would you like to edit: "))

    if x == 1:
        new_name = input("Enter the new name: ")
        assignment_List[course_code][to_be_edited]["name"] = new_name
        assignment_List[course_code][new_name] = assignment_List[course_code][to_be_edited]
        del assignment_List[course_code][to_be_edited]
    elif x == 2:
        assignment_List[course_code][to_be_edited]["due"] = input("Enter the new due date: ")
    elif x == 3:
        assignment_List[course_code][to_be_edited]["points"] = int(input("Enter the new points: "))

    with open("assignment.json", "w") as f:
        json.dump(assignment_List, f)

    return assignment_List


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    with open("classroom.json", 'r') as f:

        course = json.load(f)

    course[course_code] = {
        "course_code": course_code,
        "course_name": course_name,
        "Period": period,
        "Teacher": teacher,
        }

    with open("classroom.json", 'w') as f:
        json.dump(course, f)

    return course[course_code]


def delete_classroom(course_code: str) -> Dict:
    while True:

        with open("classroom.json", 'r') as f:
            course = json.load(f)

        try:
            del course[course_code]

        except KeyError:
            print("Course {} not found".format(course_code))
            break

        with open("classroom.json", 'w') as f:
            json.dump(course, f)

        for key, value in course.items():
            return("""
                    {}:{}
                    """.format(key, value)
                   )


def edit_classroom(course_code: str) -> Dict:
    while True:
        with open("classroom.json", 'r') as f:
            course = json.load(f)

        print(
            """
            1: Course Code
            2: Course Name
            3: Period
            4: Teacher Name
            5: Return to Course OPTIONS
            """
        )

        ask = int(input("what would you like to change:"))

        if ask is 1:
            new_course_code = input("Please enter the new Course Code:")
            course[course_code]["course_code"] = new_course_code
            with open("classroom.json", 'w') as f:
                json.dump(course, f)

            cont = input("would you like to do more edits for this course (y/n):")

            if cont == "y":
                continue
            else:
                break

        elif ask == 2:
            new_course_name = input("Please enter the new Course Name:")
            course[course_code]["course_name"] = new_course_name
            with open("classroom.json", 'w') as f:
                json.dump(course, f)

            cont = input("would you like to do more edits for this course (y/n):")

            if cont == "y":
                continue
            else:
                break

        elif ask == 3:
            new_period = int(input("Please enter the new Period:"))
            course[course_code]["Period"] = new_period
            with open("classroom.json", 'w') as f:
                json.dump(course, f)

            cont = input("would you like to do more edits for this course (y/n):")

            if cont == "y":
                continue
            else:
                break

        elif ask == 4:
            new_teacher = input("Please enter the new Teacher Name:")
            course[course_code]["Teacher"] = new_teacher
            with open("classroom.json", 'w') as f:
                json.dump(course, f)

            cont = input("would you like to do more edits for this course (y/n):")

            if cont == "y":
                continue
            else:
                break

        elif ask == 5:
            break

        else:
            print("""

            This is an invalid option. Please try again.

            """)


def calculate_average_mark(course_code: str) -> float:
    """Calculates the average mark of a student"""
    with open("classroom.json", "r") as f:
        course = json.load(f)
    with open("students.json", "r") as f:
        student_list = json.load(f)

    avg = 0
    number_of_student = 0
    for key, value in course[course_code]["Student"].items():
        avg += course[course_code]["Student"][key]["Grade"]
        number_of_student += 1

    avg = avg / number_of_student

    return avg


def add_student_to_classroom(student: str):

    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    course_code = input("Which course is the {} in:".format(student))

    gender = input("Enter {}'s gender:".format(student))

    student_number = int(input("Enter {}'s student number:".format(student)))

    email = input("Enter {}'s school email:".format(student))

    comments = input("Enter your comments:")

    number_of_marks = int(input("Please enter the number of marks you want to add:"))

    marks_list = []

    grade = 0

    grade_total = 0

    weight_total = 1
    if number_of_marks > 0:
        for i in range(number_of_marks):
            marks = float(input("Please enter the marks:"))
            weight = float(input("Please enter the weight mark of this assignment (enter as percentage, i.e 5):")) / 100
            weight_total -= weight
            marks_list.append(marks)
            grade += (marks * weight)
        grade_total = grade / number_of_marks
        grade_total += 100 * weight_total

    with open("classroom.json", "r") as f:
        course = json.load(f)

    with open("students.json", "r") as f:
        student_list = json.load(f)

    student_list[course_code] = {
        student: {
            "Student Name": student,
            "Gender": gender,
            "Studet Number": student_number,
            "Marks": marks_list,
            "Grade": grade_total,
            "Student Email": email,
            "Comments": comments
        }
    }
    course[course_code]["Students"] = student_list[course_code]

    with open("classroom.json", "w") as f:
        json.dump(course, f)

    with open("students.json", "w") as f:
        json.dump(student_list, f)

    return course[course_code]


def remove_student_from_classroom(course_code: str, student: str):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    with open("Classroom.json", "r") as f:
        course = json.load(f)

    try:
        del course[course_code]["Student"][student]
    except KeyError:
        print("Student {} not found".format(course))

    with open("classroom.json", 'w') as f:
        json.dump(course, f)

    for key, value in course.items():
        print("""

                {}:{}
                """.format(key, value))


def edit_student(course_code: str, student: str):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    while True:

        with open("classroom.json", 'r') as f:
            course = json.load(f)

        with open("students.json", 'r') as f:
            student_list = json.load(f)

        print(
            """
            Edit Student Menu
            1: Student Name
            2: Gender
            3: Student Number
            4: Marks
            5: Email
            6: Comments
            7: Return to Student OPTIONS
            """
        )

        ask = int(input("what would you like to change:"))

        if ask is 1:
            new_student_name = input("Please enter the new Student Name:")
            course[course_code]["Student"][student]["Student Name"] = new_student_name
            with open("classroom.json", 'w') as f:
                json.dump(course, f)

            cont = input("would you like to do more edits for this Student (y/n):")

            if cont == "y":
                continue
            else:
                break

        elif ask == 2:
            new_gender = input("Please enter the new gender:")
            course[course_code]["Student"][student]["Gender"] = new_gender
            with open("classroom.json", 'w') as f:
                json.dump(course, f)

            cont = input("would you like to do more edits for this Student (y/n):")

            if cont == "y":
                continue
            else:
                break

        elif ask == 3:
            new_student_number = int(input("Please enter the new Student Number:"))
            course[course_code]["Student"][student]["Student Number"] = new_student_number
            with open("classroom.json", 'w') as f:
                json.dump(course, f)

            cont = input("would you like to do more edits for this Student (y/n):")

            if cont == "y":
                continue
            else:
                break

        elif ask == 4:
            print("""
                1: Add Marks
                2: Remove marks
                3: Return to Edit Student Menu
            """)

            option = int(input("What would you like to do: "))

            marks = student_list[student]["Marks"]
            grade_total = student_list[student]["Grade"]
            grade = 0
            weight_total = 0
            if option == 1:

                number_of_marks = int(input("How many marks do you want to add:"))

                for i in range(number_of_marks):

                    new_marks = float(input("Enter new Marks:"))

                    weight = float(input("What is the weight: "))

                    weight_total += weight

                    grade += (marks * weight)

                    marks.append(new_marks)

                weight_remander = 1 - weight_total

                grade_total = (((grade / number_of_marks) + (100 * weight_remander)) + (grade_total)) / 2

                marks.sort()

                course[course_code]["Students"][student]["Marks"] = marks

                with open("student.json", "w") as f:
                    json.dump(student_list, f)

                with open("classroom.json", "w") as f:
                    json.dump(course, f)

                cont = input("would you like to do more edits for this Student (y/n):")

                if cont == "y":
                    continue
                else:
                    break

            if option == 2:

                number_of_marks_remove = int(input("How many marks are you removing:"))

                for i in range(number_of_marks_remove):

                    remove_marks = float(input("Enter new Marks:"))

                    weight = float(input("What is the weight: "))

                    weight_total += weight

                    grade += (marks * weight)

                    marks.remove(new_marks)

                weight_remander = 1 - weight_total

                grade_total = ((grade_total) - ((grade / number_of_marks) + (100 * weight_remander))) / 2

                cont = input("would you like to do more edits for this Student (y/n):")

                if cont == "y":
                    continue
                else:
                    break

        elif ask == 5:
            new_email = input("Please enter the new Student Email:")
            course[course_code]["Student"][student]["Student Email"] = new_email
            with open("classroom.json", 'w') as f:
                json.dump(course, f)

            cont = input("would you like to do more edits for this Student (y/n):")

            if cont == "y":
                continue
            else:
                break

        elif ask == 6:
            new_comment = input("Please enter the new comment:")
            course[course_code]["Student"][student]["Comment"] = new_comment
            with open("classroom.json", 'w') as f:
                json.dump(course, f)

            cont = input("would you like to do more edits for this Student (y/n):")

            if cont == "y":
                continue
            else:
                break

        elif ask == 7:
            break
        else:
            print("""

            This is an invalid option. Please try again.

            """)

    pass
