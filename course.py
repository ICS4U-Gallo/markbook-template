# Create student global dict then create a course   
student = {}
assignment = {}
course = {'course_code': None, 'course_name': None, 'period': None, 'teacher': None, 'student_list': student, 'assignment_list': assignment}

# Allow user to edit course details
print(course)
course_edit = input("What would you like to edit? (Enter c for course code, n for course name, p for period, t for teacher, s for student list, and a for list of assignments ")

if course_edit == "c":

# editing course code
  course_code = input("Would you like you replace or delete the course code? (Enter rc to replace and dc to delete) ")
  if course_code == "rc":
    new_course_code = input("Enter the replacement: ")
    course['course_code'] = new_course_code
    print(course)
  elif course_code == "dc":
    course['course_code'] = None
    print(course)

# editing course name
elif course_edit == "n":
  course_name = input("Would you like to replace or delete the course name? (Enter rn to replace and dn to delete) ")
  if course_name == "rn":
    new_course_name = input("Enter the replacement: ")
    course['course_name'] = new_course_name
    print(course)
  elif course_name == "dn":
    course['course_name'] = None
    print(course)

# editing period
elif course_edit == "p":
  period = input("Would you like to replace or delete the period number? (Enter rp to replace and dp to delete) ")
  if period == "rp":
    new_period = int(input("Enter the replacement: "))
    course['period'] = new_period
    print(course)
  elif period == "dp":
    course['period'] = None
    print(course)

# editing teacger
elif course_edit == "t":
  teacher = input("Would you like to replace or delete the teacher's name? (Enter rt to replace and dt to delete) ")
  if teacher == "rt":
    new_teacher = input("Enter the replacement: ")
    course['teacher'] = new_teacher
    print(course)
  elif teacher == "dt":
    course['teacher'] = None
    print(course)

# set configurations for student list

# Create errors (what happens if the user does not enter any of the right commands?)





 
