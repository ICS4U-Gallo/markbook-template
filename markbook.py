"""
Markbook Application
Group members: Alex, Aryan, Ryan
"""

from typing import Dict


def create_student(first_name: str, last_name: str) -> Dict:
    """Create student information represented in a dictionary

    Args:
        first_name: first name of the student
        last_name: last name of the student
    Returns:
        Student information as a dictionary
    """
    student = {
        "first_name": first_name,
        "last_name": last_name,
        "assignment_list": []
    }

    return student


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary

    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    return {"name": name,
            "due": due,
            "points": points}


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    classroom = {"course_code": course_code,
                 "course_name": course_name,
                 "period": period,
                 "teacher": teacher,
                 "student_list": [],
                 "assignment_list": []}
    return classroom


def calculate_average_mark(student: Dict, classroom: Dict) -> float:
    """Calculates the average mark of a student"""

    sum = 0
    length = len(student["assignment_list"])

    if length is not 0:

        for i in range(length):

            numerator = student["assignment_list"][i]["points"]
            denumerator = classroom["assignment_list"][i]["points"]

            sum += int(numerator) / int(denumerator)

        return sum / length

    else:
        return -1


def add_student_to_classroom(student: Dict, classroom: Dict):
    # Adds student to a classroom
    classroom["student_list"].append(student)
    pass


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    classroom["student_list"].remove(student)
    pass


def edit_student(student: Dict, kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    for key, value in kwargs.items():
        student[key] = value
    pass
