"""
Markbook Application
Group members: Joseph, Joshua
"""
import json
from typing import Dict

# Students:
# first_name: str
# last_name: str
# gender: str
# image: filepath: str
# student number: int
# grade: int
# email: str
# marks: list[float]
# comments: str
# Class
# course_code: str
# course_name: str
# period: int
# teacher_name: str
# student_list: list[dict]
# assignments_list: list[dict]
# Assignments
# due: str
# name: str
# points: int


def create_student(first_name: str, last_name: str,
                   gender: str, image: str,
                   student_number: int, grade: int,
                   email: str) -> Dict:
    """Creates a student dictionary"""
    return {"first_name": first_name, "last_name": last_name,
            "gender": gender, "image": image, "student_number":
            student_number, "grade": grade, "email": email, "classes": {}}


def create_assignment(name: str, due: str, points: int, weight: int) -> Dict:
    """Creates an assignment represented as a dictionary

    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
        weight: how much the assignment is worth (percentage)
    Returns:
        Assignment as a dictionary.
    """
    return {"name": name, "due": due, "points": points, "weight": weight}


def create_classroom(course_code: str, course_name: str,
                     period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""

    return {"course_code": course_code, "course_name": course_name,
            "period": period, "teacher": teacher, "student_list": [],
            "assignment_list": [], "student_marks": {}}


def calculate_student_average(student: Dict) -> float:
    """Calculates the average mark of a student"""

    marks = student["classes"]
    average = 0.0
    class_counter = 0

    for mark in marks.values():
        if mark is None:
            average += mark
            class_counter += 1

    if class_counter != 0:
        average /= class_counter
        return f"{round(average, 1)}%"
    else:
        return "none. No marks recorded"


def calculate_class_average(classroom: Dict) -> float:
    """Calculates the average mark of a class"""

    marks = classroom["student_marks"]
    average = 0.0
    student_counter = 0

    for mark in marks.values():
        if mark is None:
            average += mark
            student_counter += 1

    if student_counter != 0:
        average /= len(marks)
        return f"{round(average, 1)}%"
    else:
        return "none. No marks recorded"


def add_student_to_classroom(student, classroom):
    """Adds student to a classroom

    Args:
        student: Student info dict
        classroom: The classroom to add the student to
    """

    first_name = student["first_name"]
    last_name = student["last_name"]
    name = f"{first_name} {last_name}"

    classroom["student_list"].append(name)
    classroom["student_marks"][name] = None
    student["classes"][classroom["course_code"]] = None


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed (dict)
        classroom: the class from which the student will be removed.
    """
    first_name = student["first_name"]
    last_name = student["last_name"]
    name = f"{first_name} {last_name}"

    classroom["student_list"].remove(name)
    del classroom["student_marks"][name]
    del student["classes"][classroom["course_code"]]


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be updated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    for key, value in kwargs.items():
        student[key] = value


# Loading in file

loading_file = True
tried_to_load = False

while loading_file:
    if tried_to_load is False:
        load_file = input(
            "Would you like to load in a file?\n[Y]Yes [N]No\n").upper()

    if load_file == "Y":
        while loading_file:
            file_name = str(input(
                "\nPlease enter the file name. (The JSON file must be in this folder.)\n"))
            try:
                with open(file_name, "r") as f:
                    data = json.load(f)
            except:
                print("\nFile does not exist in this folder.\n")
                load_file = input(
                    "Would you like to try again?\n[Y]Yes [N]No\n").upper()
                tried_to_load = True
                break
            else:
                print("\nFile successfully loaded.")
                loading_file = False

    elif load_file == "N":
        data = {
            "student_List": [],
            "student_Info": {},
            "classroom_List": [],
            "classroom_Info": {}
        }

        loading_file = False

# Menu

while True:
    print("\n\nWhat would you like to do?")
    try:
        category = int(input("\n [0] Create new information"
                             "\n [1] Edit current information"
                             "\n [2] Preview saved information"
                             "\n [3] Exit\n"))
    except:
        print("\nPlease enter a number from the categories below.")
    else:
        if category not in range(0, 4):
            print("\nPlease enter a number from the categories below.")
        elif category == 0:
            while True:
                print("\n\nCreate new information")
                try:
                    selection = int(input("\n [0] Register Student"
                                          "\n [1] Create Classroom"
                                          "\n [2] Create Assignment"
                                          "\n [3] Back\n"))
                except:
                    print(
                        "Please enter a number from the selection above.\n")
                else:
                    if selection not in range(0, 4):
                        print(
                            "Please enter a number from the selection above.\n")

                    elif selection == 0:
                        print("\n\nRegister Student\n")
                        while True:
                            first_name = str(
                                input("Please enter the student's first name: "))
                            if first_name != "":
                                break
                        while True:
                            last_name = str(
                                input("Please enter the student's last name: "))
                            if last_name != "":
                                break
                        while True:
                            gender = str(
                                input("Please enter the student's gender: "))
                            if gender != "":
                                break
                        while True:
                            image = str(
                                input("Please enter the student's image: "))
                            if image != "":
                                break
                        while True:
                            try:
                                student_number = int(
                                    input("Please enter the student's student number: "))
                            except:
                                print("Please enter a number.")
                            else:
                                break
                        while True:
                            try:
                                grade = int(
                                    input("Please enter the student's grade: "))
                            except:
                                print("Please enter a number.")
                            else:
                                break
                        while True:
                            email = str(
                                input("Please enter student's email: "))
                            if email != "":
                                break

                        full_name = f"{first_name} {last_name}"
                        data["student_Info"][full_name] = create_student(
                            first_name, last_name, gender, image, student_number, grade, email)

                        data["student_List"].append(full_name)
                        print("\nStudent successfully registered.")

                    elif selection == 1:
                        print("\n\nCreate Classroom\n")
                        while True:
                            course_code = str(
                                input("Please enter the course code: "))
                            if course_code != "":
                                break
                        while True:
                            course_name = str(
                                input("Please enter the course name: "))
                            if course_name != "":
                                break
                        while True:
                            try:
                                period = int(
                                    input("Please enter the period of the class: "))
                            except:
                                print("Please enter a number.")
                            else:
                                break
                        while True:
                            teacher = str(
                                input("Please enter the name of the teacher: "))
                            if teacher != "":
                                break

                        data["classroom_Info"][course_code] = create_classroom(
                            course_code, course_name, period, teacher)

                        data["classroom_List"].append(course_code)
                        print("\nClass successfully registered.")

                    elif selection == 2:
                        if len(data["classroom_List"]) != 0:
                            print("\n\nCreate Assignment\n")
                            while True:
                                class_code = str(input(
                                    "Which class is this assignment for? (Please enter class code)\n"))
                                if class_code in data["classroom_List"]:
                                    while True:
                                        name = str(
                                            input("\nEnter the assignment title: "))
                                        if name != "":
                                            break
                                    while True:
                                        due_date = str(
                                            input("Enter the due date: "))
                                        if due_date != "":
                                            break
                                    while True:
                                        try:
                                            points = int(
                                                input("Enter how many points is this assignment out of: "))
                                        except:
                                            print(
                                                "Please enter a number.")
                                        else:
                                            break
                                    while True:
                                        try:
                                            weight = int(
                                                input("How much is the assignment worth: "))
                                        except:
                                            print(
                                                "Please enter a number.")
                                        else:
                                            break

                                    assignment = create_assignment(
                                        name, due_date, points, weight)
                                    data["classroom_Info"][class_code]["assignment_list"].append(
                                        assignment)
                                    print("\nNew assignment created.")

                                else:
                                    print(
                                        "\nThere is currently no class with this course code running.\n")
                                    break
                        else:
                            print(
                                "\nThere are currently no classes running.")

                    elif selection == 3:
                        break

        elif category == 1:
            while True:
                print("\n\nEdit current information")
                try:
                    selection = int(input("\n [0] Add Student to Classroom"
                                          "\n [1] Edit Student Information"
                                          "\n [2] Remove student from Classroom"
                                          "\n [3] Back\n"))
                except:
                    print(
                        "Please enter a number from the selection above.")
                else:
                    if selection not in range(0, 4):
                        print(
                            "Please enter a number from the selection above.")

                    elif selection == 0:
                        if len(data["student_List"]) != 0:
                            if len(data["classroom_List"]) != 0:
                                print("\n\nAdd Student to Class\n")
                                while True:
                                    student = input(
                                        "Please enter the student's first and last name\n")
                                    if student in data["student_List"]:
                                        break
                                while True:
                                    selected_class = input(
                                        f"\nWhich class would you like to put {student}? (Course code)\n")
                                    if selected_class in data["classroom_List"]:
                                        if student in data["classroom_Info"][selected_class]["student_list"]:
                                            print(
                                                f"\n{student} is already in this class.")
                                        else:
                                            teacher = data["classroom_Info"][selected_class]["teacher"]
                                            period_num = data["classroom_Info"][selected_class]["period"]
                                            break

                                while True:
                                    confirmation = input(
                                        f"\nAre you sure you want to put {student} in {selected_class} with {teacher} for period {period_num}?\n[Y]Yes [N]No\n").upper()
                                    if confirmation == "Y":
                                        add_student_to_classroom(
                                            data["student_Info"][student], data["classroom_Info"][selected_class])
                                        print(
                                            "\nStudent added to classroom.")
                                        break
                                    elif confirmation == "N":
                                        secondary_confirmation = input(
                                            "\nWould you like to discard changes?\n[Y]Yes [N]No\n").upper()
                                        if secondary_confirmation == "Y":
                                            print(
                                                "\nDiscarding changes...")
                                            break
                            else:
                                print("There are no classes running.")
                        else:
                            print("There are no registered students.")

                    elif selection == 1:
                        if len(data["student_List"]) != 0:
                            while True:
                                student = input(
                                    "\nWhich student's information would you like to change? (First name and last name)\n")
                                if student in data["student_List"]:
                                    changes_dict = (data["student_Info"]
                                                    [student]).copy()
                                    break
                                else:
                                    print(
                                        "\nPlease enter a registered student.")

                            while True:
                                first_name = changes_dict["first_name"]
                                try:
                                    selection = int(
                                        input("\n\nWhat would you like to change?\n"
                                              "\n [0] First Name"
                                              "\n [1] Last Name"
                                              "\n [2] Gender"
                                              "\n [3] Image"
                                              "\n [4] Student Number"
                                              "\n [5] Grade"
                                              "\n [6] Email"
                                              "\n [7] Display Current Info"
                                              "\n [8] Exit\n"))
                                except:
                                    print(
                                        "Please enter a number from the selection above.\n")
                                else:
                                    if selection not in range(0, 9):
                                        print(
                                            "Please enter a number from the selection above.\n")
                                    elif selection == 0:
                                        while True:
                                            change = input(
                                                f"\nWhat would you like to change {first_name}'s first name to?\n")
                                            confirmation = input(
                                                f"\nAre you sure you want to change {first_name}'s first name to {change}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                changes_dict["first_name"] = change
                                                break
                                            elif confirmation == "N":
                                                print(
                                                    "\nChange discarded")
                                                break

                                    elif selection == 1:
                                        while True:
                                            change = input(
                                                f"\nWhat would you like to change {first_name}'s last name to?\n")
                                            confirmation = input(
                                                f"\nAre you sure you want to change {first_name}'s last name to {change}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                changes_dict["last_name"] = change
                                                break
                                            elif confirmation == "N":
                                                print(
                                                    "\nChange discarded")
                                                break

                                    elif selection == 2:
                                        while True:
                                            change = input(
                                                f"\nWhat would you like to change {first_name}'s gender to?\n")
                                            confirmation = input(
                                                f"\nAre you sure you want to change {first_name}'s gender to {change}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                changes_dict["gender"] = change
                                                break
                                            elif confirmation == "N":
                                                print(
                                                    "\nChange discarded")
                                                break

                                    elif selection == 3:
                                        while True:
                                            change = input(
                                                f"\nWhat would you like to change {first_name}'s image to?\n")
                                            confirmation = input(
                                                f"\nAre you sure you want to change {first_name}'s image to {change}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                changes_dict["image"] = change
                                                break
                                            elif confirmation == "N":
                                                print(
                                                    "\nChange discarded")
                                                break

                                    elif selection == 4:
                                        while True:
                                            change = input(
                                                f"\nWhat would you like to change {first_name}'s student number to?\n")
                                            confirmation = input(
                                                f"\nAre you sure you want to change {first_name}'s student number to {change}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                changes_dict["student_number"] = change
                                                break
                                            elif confirmation == "N":
                                                print(
                                                    "\nChange discarded")
                                                break

                                    elif selection == 5:
                                        while True:
                                            change = input(
                                                f"\nWhat would you like to change {first_name}'s grade to?\n")
                                            confirmation = input(
                                                f"\nAre you sure you want to change {first_name}'s grade to {change}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                changes_dict["grade"] = change
                                                break
                                            elif confirmation == "N":
                                                print(
                                                    "\nChange discarded")
                                                break

                                    elif selection == 6:
                                        while True:
                                            change = input(
                                                f"\nWhat would you like to change {first_name}'s email to?\n")
                                            confirmation = input(
                                                f"\nAre you sure you want to change {first_name}'s email to {change}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                changes_dict["email"] = change
                                                break
                                            elif confirmation == "N":
                                                print(
                                                    "\nChange discarded")
                                                break

                                    elif selection == 7:
                                        if changes_dict != data["student_Info"][student]:
                                            chg_f_name = changes_dict["first_name"]
                                            chg_l_name = changes_dict["last_name"]
                                            new_name = f"{chg_f_name} {chg_l_name}"

                                            if new_name != student and len(data["student_Info"][student]["classes"]) != 0:
                                                for classroom in data["student_Info"][student]["classes"].keys():
                                                    student_list = data["classroom_Info"][classroom]["student_list"]
                                                    student_list.append(
                                                        new_name)
                                                    student_list.remove(
                                                        student)

                                                    student_marks = data["classroom_Info"][classroom]["student_marks"]
                                                    student_marks[new_name] = student_marks[student]
                                                    del student_marks[student]

                                            edit_student(
                                                data["student_Info"][student], **changes_dict)
                                            data["student_List"].append(
                                                new_name)
                                            data["student_List"].remove(
                                                student)

                                            data["student_Info"][new_name] = data["student_Info"][student].copy(
                                            )
                                            del data["student_Info"][student]

                                        print(
                                            "\n\nPreviewing Information\n")
                                        for key, value in data["student_Info"][student].items():
                                            if key == "first_name":
                                                print(
                                                    f"First name: {value}")
                                            elif key == "last_name":
                                                print(
                                                    f"Last name: {value}")
                                            elif key == "gender":
                                                print(
                                                    f"Gender: {value}")
                                            elif key == "image":
                                                print(
                                                    f"Image: {value}")
                                            elif key == "student_number":
                                                print(
                                                    f"Student number: {value}")
                                            elif key == "grade":
                                                print(
                                                    f"Grade: {value}")
                                            elif key == "email":
                                                print(
                                                    f"Email: {value}")
                                            elif key == "classes":
                                                if value == {}:
                                                    print(
                                                        "Classes: None")
                                                else:
                                                    print(
                                                        f"Classes: {value}")
                                        input(
                                            "Press enter when you're done viewing.")

                                    elif selection == 8:
                                        if changes_dict != data["student_Info"][student]:
                                            chg_f_name = changes_dict["first_name"]
                                            chg_l_name = changes_dict["last_name"]
                                            new_name = f"{chg_f_name} {chg_l_name}"

                                            if new_name != student and len(data["student_Info"][student]["classes"]) != 0:
                                                for classroom in data["student_Info"][student]["classes"].keys():
                                                    student_list = data["classroom_Info"][classroom]["student_list"]
                                                    student_list.append(
                                                        new_name)
                                                    student_list.remove(
                                                        student)

                                                    student_marks = data["classroom_Info"][classroom]["student_marks"]
                                                    student_marks[new_name] = student_marks[student]
                                                    del student_marks[student]

                                            edit_student(
                                                data["student_Info"][student], **changes_dict)
                                            data["student_List"].append(
                                                new_name)
                                            data["student_List"].remove(
                                                student)

                                            data["student_Info"][new_name] = data["student_Info"][student].copy(
                                            )
                                            del data["student_Info"][student]
                                        print("\nSaved all changes")
                                        break
                        else:
                            print(
                                "\nThere are currently no registered students.")
                            break

                    elif selection == 2:
                        if len(data["classroom_List"]) != 0:
                            if len(data["student_List"]) != 0:
                                print("\n\nRemove Student From Class\n")
                                while True:
                                    selected_class = input(
                                        "Which class would you like to choose? (Please enter the class code)\n")
                                    if selected_class in data["classroom_List"]:
                                        break

                                while True:
                                    student = input(
                                        f"\nWhich student would you like to remove from {selected_class}? (Please enter student's first and last name)\n")
                                    if student not in data["student_List"]:
                                        print(
                                            f"\nThere is no student by the name of {student} registered.")
                                        break
                                    elif student not in data["classroom_Info"][selected_class]["student_list"]:
                                        print(
                                            f"\n{student} is not attending this class.")
                                        break
                                    else:
                                        while True:
                                            confirmation = input(
                                                f"\nAre you sure you want to remove {student} from {selected_class}?\n[Y]Yes [N]No\n").upper()
                                            if confirmation == "Y":
                                                remove_student_from_classroom(
                                                    data["student_Info"][student], data["classroom_Info"][selected_class])
                                                print(
                                                    "\nStudent removed from class.")
                                                break
                                            elif confirmation == "N":
                                                break
                                        break
                            else:
                                print(
                                    "There are currently no registered students.")
                        else:
                            print(
                                "There are no classes currently running.")

                    elif selection == 3:
                        break

        elif category == 2:
            while True:
                print("\n\nPreview Information")
                try:
                    selection = int(
                        input("\n [0] Student List"
                              "\n [1] Classroom List"
                              "\n [2] Student Average Mark"
                              "\n [3] Class Average Mark"
                              "\n [4] Student Info"
                              "\n [5] Classroom Info"
                              "\n [6] Back\n "))
                except:
                    print(
                        "\nPlease enter a number from the selection above.")
                else:
                    if selection not in range(0, 7):
                        print(
                            "\nPlease enter a number from the selection above.\n")

                    elif selection == 0:
                        print("")
                        if len(data["student_List"]) != 0:
                            for student in data["student_List"]:
                                print(student)
                            input(
                                "\nPress enter why you're done viewing.")
                        else:
                            print("No students registered.")

                    elif selection == 1:
                        if len(data["classroom_List"]) != 1:
                            for class_code in data["classroom_List"]:
                                print(class_code)
                            input(
                                "\nPress enter why you're done viewing.")
                        else:
                            print("No classes registered.")

                    elif selection == 2:
                        if len(data["student_List"]) != 0:
                            if len(data["classroom_List"]) != 0:
                                while True:
                                    print(
                                        "\n\nStudent Average Mark\n")
                                    student = input(
                                        "Which student would you like to choose? (Please enter first and last name)\n")
                                    if student in data["student_List"]:
                                        if len(data["student_Info"][student]["classes"]) != 0:
                                            student_average = calculate_student_average(
                                                data["student_Info"][student])
                                            print(
                                                f"\n{student}'s average is {student_average}.")
                                        else:
                                            print(
                                                f"\n{student} is currently not attending any classes.")
                                        break
                                    else:
                                        print(
                                            "\nPlease enter a registered student.")
                            else:
                                print(
                                    "\nThere are currently no classes running.")
                        else:
                            print(
                                "\nThere are currently no registered students.")

                    elif selection == 3:
                        if len(data["classroom_List"]) != 0:
                            if len(data["student_List"]) != 0:
                                while True:
                                    print("\n\nClass Average Mark\n")
                                    selected_class = input(
                                        "Which class would you like to choose? (Please enter the class code)\n")
                                    if selected_class in data["classroom_List"]:
                                        if len(data["classroom_Info"][selected_class]["student_list"]) != 0:
                                            class_average = calculate_class_average(
                                                data["classroom_Info"][selected_class])
                                            print(
                                                f"\nThe class average for {selected_class} is {class_average}.")
                                        else:
                                            print(
                                                "\nThere are no students attending this class.")
                                        break
                                    else:
                                        print(
                                            "\nPlease enter a registered class.")
                            else:
                                print(
                                    "\nThere are currently no registered students.")
                        else:
                            print(
                                "\nThere are currently no classes running.")

                    elif selection == 4:
                        if len(data["student_List"]) != 0:
                            while True:
                                print("\n\nStudent Info\n")
                                student = input(
                                    "Please enter student's first and last name.\n")
                                if student in (data["student_List"]):
                                    for key, value in data["student_Info"][student].items():
                                        if key == "first_name":
                                            print(
                                                f"First name: {value}")
                                        elif key == "last_name":
                                            print(
                                                f"Last name: {value}")
                                        elif key == "gender":
                                            print(f"Gender: {value}")
                                        elif key == "image":
                                            print(f"Image: {value}")
                                        elif key == "student_number":
                                            print(
                                                f"Student number: {value}")
                                        elif key == "grade":
                                            print(f"Grade: {value}")
                                        elif key == "email":
                                            print(f"Email: {value}")
                                        elif key == "classes":
                                            if value == {}:
                                                print("Classes: None")
                                            else:
                                                print(
                                                    f"Classes: {value}")
                                    input(
                                        "\nPress enter when you're done viewing.")
                                    break
                                else:
                                    print(
                                        "\nPlease enter a registered student.")
                        else:
                            print(
                                "\nThere are currently no registered students.")

                    elif selection == 5:
                        if len(data["classroom_List"]) != 0:
                            while True:
                                print("\n\nClass Information\n")
                                selected_class = input(
                                    "Which class would you like to choose? (Please enter the class code)\n")
                                if selected_class in data["classroom_List"]:
                                    for key, value in data["classroom_Info"][selected_class].items():
                                        if key == "course_code":
                                            print(
                                                f"Course code: {value}")
                                        elif key == "course_name":
                                            print(
                                                f"Course name: {value}")
                                        elif key == "period":
                                            print(f"Period: {value}")
                                        elif key == "teacher":
                                            print(f"Teacher: {value}")
                                        elif key == "student_list":
                                            if value == {}:
                                                print(
                                                    "Student list: None")
                                            else:
                                                print(
                                                    f"Student list: {value}")
                                        elif key == "assignment_list":
                                            if value == {}:
                                                print(
                                                    "Assignment list: None")
                                            else:
                                                print(
                                                    f"Assignment list: {value}")
                                        elif key == "student_marks":
                                            if value == {}:
                                                print(
                                                    "Student marks: None")
                                            else:
                                                print(
                                                    f"Student mark: {value}")

                                    input(
                                        "\nPress enter when you're done viewing.")
                                    break
                                else:
                                    print(
                                        "\nPlease enter a registered class.")
                        else:
                            print(
                                "\nThere are currently no classes running.")

                    elif selection == 6:
                        break

        elif category == 3:
            save = input(
                "\nWould you like to save your changes?\n[Y]Yes [N]No\n").upper()
            if save == "Y"and load_file == "N":
                file_name = ""
                while file_name == "":
                    file_name = str(
                        input("What would you like to name the new file?\n"))
                while True:
                    confirmation = input(
                        f"Are you sure you want to save all changes in {file_name}.json?\n[Y]Yes [N]No\n").upper()
                    if confirmation == "Y":
                        if ".json" not in file_name:
                            file_name += ".json"
                            load_file = "Y"
                    break

            elif save == "N":
                while True:
                    secondary_confirmation = input(
                        "\nAre you sure you want to discard all the changes?\n[Y]Yes [N]No\n").upper()
                    if secondary_confirmation == "Y":
                        print("\nDiscarding changes\n")
                        exit()
                    elif secondary_confirmation == "N":
                        break

            if load_file == "Y":
                with open(file_name, "w") as f:
                    json.dump(data, f, indent=4)

                print("Saved all changes.")
                exit()
