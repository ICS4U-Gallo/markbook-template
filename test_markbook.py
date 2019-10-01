import pytest
import markbook

course = markbook.course("Comp Sci", "ICS4U1", "2", "Gallo")
student = markbook.student("Eric", "Jeng", 1036010)


def test_create_student():
    assert isinstance(student, markbook.student)
    assert student.first == "Eric"
    assert student.last == "Jeng"
    assert student.stu_num == 1036010


def test_create_course():
    assert isinstance(course, markbook.course)
    assert course.name == "Comp Sci"
    assert course.code == "ICS4U1"
    assert course.period == "2"
    assert course.teacher == "Gallo"


def test_create_assignment():
    assignment = markbook.assignment("Markbook", "Oct. 2, 2019", 40,
                                     course.code)
    assert isinstance(assignment, markbook.assignment)
    assert assignment.name == "MARKBOOK"
    assert assignment.due == "Oct. 2, 2019"
    assert assignment.point == 40
    assert assignment.course == "ICS4U1"


def test_add_student_to_course():
    course.add_student(student)
    assert len(course.students_list) == 1
    assert len(student.course_list) == 1


'''
@pytest.mark.skip()
def test_create_assigment():
    assignment1 = markbook.create_assignment(name="Assignment One",
                                            due="2019-09-21",
                                            points=100)
    expected = {
        "name": "Assignment One",
        "due": "2019-09-21",
        "points": 100
    }
    assert assignment1 == expected

    assignment2 = markbook.create_assignment(name="Assignment Two",
                                             due=None,
                                             points=1)
    assert assignment2["name"] == "Assignment Two"
    assert assignment2["due"] is None
    assert assignment2["points"] == 1


@pytest.mark.skip()
def test_create_classroom():
    classroom = markbook.create_classroom(course_code="ICS4U",
                                          course_name="Computer Science",
                                          period=2,
                                          teacher="Mr. Gallo")
    expected = {
        "course_code": "ICS4U",
        "course_name": "Computer Science",
        "period": 2,
        "teacher": "Mr. Gallo"
    }

    # The classroom needs to be a dictionary identical to the expected
    assert classroom == expected

    # The classroom needs to be created with
    # empty lists for students and assignments
    assert classroom["student_list"] == []
    assert classroom["assignment_list"] == []


@pytest.mark.skip
def test_calculate_average_mark():
    student = {
        "marks": [50, 100]
    }
    assert markbook.calculate_average_mark(student) == 75.0


@pytest.mark.skip
def test_add_student_to_classroom():
    """
    Dependencies:
        - create_classroom()
    """
    classroom = markbook.create_classroom(course_code="ICS4U",
                                          course_name="Computer Science",
                                          period=2,
                                          teacher="Mr. Gallo")
    student = {"first_name": "John", "last_name": "Smith"}

    assert len(classroom["student_list"]) == 0
    markbook.add_student_to_classroom(student, classroom)
    assert type(classroom["student_list"]) is list
    assert len(classroom["student_list"]) == 1


@pytest.mark.skip
def test_remove_student_from_classroom():
    """
    Dependencies:
        - create_classroom()
        - add_student_to_classroom()
    """
    classroom = markbook.create_classroom(course_code="ICS4U",
                                          course_name="Computer Science",
                                          period=2,
                                          teacher="Mr. Gallo")
    student = {"first_name": "John", "last_name": "Smith"}

    markbook.add_student_to_classroom(student, classroom)
    assert len(classroom["student_list"]) == 1
    markbook.remove_student_from_classroom(student, classroom)
    assert type(classroom["student_list"]) is list
    assert len(classroom["student_list"]) == 0


@pytest.mark.skip
def test_edit_student():
    student = {"first_name": "John", "last_name": "Smith", "grade": 10}
    markbook.edit_student(student, first_name="Frank", last_name="Bell")
    assert student["first_name"] == "Frank"
    assert student["last_name"] == "Bell"
    assert student["grade"] == 10
'''
