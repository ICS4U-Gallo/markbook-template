import pytest

import markbook


def test_create_student():
    student1 = markbook.create_student(first_name = "Josh", last_name = "2", 
                                       gender = "Male", image = "Josh.jpeg",
                                       student_number = 6479299892, grade = 11,
                                       email = "joshthegreatsayshi@gmail.com")

    expected = {
        "first_name": "Josh", "last_name": "2",
        "gender": "Male", "image": "Josh.jpeg",
        "student_number": 6479299892, "grade": 11,
        "email": "joshthegreatsayshi@gmail.com", "classes": {}
    }
    assert student1 == expected

    student2 = markbook.create_student(first_name = "Linda", last_name = "3",
                                       gender = "Female", image = "Linda.jpeg",
                                       student_number = 123456789, grade = 10,
                                       email = "linda.322@ycdsbk12.ca")
    assert student2["first_name"] == "Linda"
    assert student2["student_number"] == 123456789
    assert student2["email"] == "linda.322@ycdsbk12.ca"



def test_create_assignment():
    assignment1 = markbook.create_assignment(name="Assignment One",
                                             due="2019-09-21",
                                             points=100,
                                             weight=5)
    expected = {
        "name": "Assignment One",
        "due": "2019-09-21",
        "points": 100,
        "weight": 5
    }
    assert assignment1 == expected

    assignment2 = markbook.create_assignment(name="Assignment Two",
                                             due=None,
                                             points=1,
                                             weight= 20)
    assert assignment2["name"] == "Assignment Two"
    assert assignment2["due"] is None
    assert assignment2["points"] == 1
    assert assignment2["weight"] == 20



def test_create_classroom():
    classroom = markbook.create_classroom(course_code = "ICS4U",
                                          course_name = "Computer Science",
                                          period = 2,
                                          teacher = "Mr. Gallo")
    expected = {
        "course_code": "ICS4U",
        "course_name": "Computer Science",
        "period": 2,
        "teacher": "Mr. Gallo",
        "student_list": [],
        "student_marks": {},
        "assignment_list": []
    }

    # The classroom needs to be a dictionary identical to the expected
    assert classroom == expected

    # The classroom needs to be created with
    # empty lists for students and assignments,
    # empty dictionary for students and their marks
    assert classroom["student_list"] == []
    assert classroom["assignment_list"] == []
    assert classroom["student_marks"] == {}


def test_calculate_student_average():
    student = markbook.create_student(first_name="John", last_name="Smith",
                                      gender="Male", image="jsmith.png", 
                                      student_number=111, grade=9, 
                                      email="john.smith23@ycdsbk12.ca")
    student["classes"]["ICS4U"] = 84.42
    student["classes"]["MHF4U"] = 90.0

    assert markbook.calculate_student_average(student) == 87.2


def test_class_average():
    classroom = markbook.create_classroom(course_code = "ICS4U",
                                          course_name = "Computer Science",
                                          period = 2,
                                          teacher = "Mr. Gallo")
    classroom["student_marks"]["John"] = 80.0
    classroom["student_marks"]["Jane"] = 90.0

    assert markbook.calculate_class_average(classroom) == 85.0



def test_add_student_to_classroom():
    """
    Dependencies:
        - create_student
        - create_classroom()
    """
    student_Info = {"John Smith": markbook.create_student(first_name="John", last_name="Smith",
                                                          gender="Male", image="jsmith.png", 
                                                          student_number=111, grade=9, 
                                                          email="john.smith23@ycdsbk12.ca")}
    classroom_Info = {"ICS4U": markbook.create_classroom(course_code="ICS4U",
                                                         course_name="Computer Science",
                                                         period=2,
                                                         teacher="Mr. Gallo")}

    assert len(classroom_Info["ICS4U"]["student_list"]) == 0
    markbook.add_student_to_classroom(student_Info["John Smith"], classroom_Info["ICS4U"])
    assert type(classroom_Info["ICS4U"]["student_list"]) is list
    assert classroom_Info["ICS4U"]["student_list"] == ["John Smith"]
    # check that student mark is set to none
    assert student_Info["John Smith"]["classes"] == {"ICS4U": None}



def test_remove_student_from_classroom():
    """
    Dependencies:
        - create_classroom()
        - add_student_to_classroom()
    """
    student_Info = {"John Smith": markbook.create_student(first_name="John", last_name="Smith",
                                                          gender="Male", image="jsmith.png", 
                                                          student_number=111, grade=9, 
                                                          email="john.smith23@ycdsbk12.ca")}
    classroom_Info = {"ICS4U": markbook.create_classroom(course_code="ICS4U",
                                                         course_name="Computer Science",
                                                         period=2,
                                                         teacher="Mr. Gallo")}
    markbook.add_student_to_classroom(student_Info["John Smith"], classroom_Info["ICS4U"])
    assert len(classroom_Info["ICS4U"]["student_list"]) == 1
    markbook.remove_student_from_classroom(student_Info["John Smith"], classroom_Info["ICS4U"])
    assert type(classroom_Info["ICS4U"]["student_list"]) is list
    assert len(classroom_Info["ICS4U"]["student_list"]) == 0
    assert len(student_Info["John Smith"]["classes"]) == 0



def test_edit_student():
    student = {"first_name": "John", "last_name": "Smith", "grade": 10}
    markbook.edit_student(student, first_name="Frank", last_name="Bell")
    assert student["first_name"] == "Frank"
    assert student["last_name"] == "Bell"
    assert student["grade"] == 10
