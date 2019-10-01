from markbook import *
from data_managment_methods import *
import time
import os


class user_interface_controller:
    """Class obj that interacts with the user to fufill requests"""

    def __init__(self, class_data, filename):
        self.filename = filename
        self.data = class_data

    def help(self):
        print("""\nCommands List:
        --> exit
        --> help
        --> clear
        --> save
        --> add-student
        --> remove-student
        --> add-assignment
        --> add-student-mark
        --> show-assignment
        --> calculate-student-avg
        --> show-students
        --> edit-student-info\n""")

    def add_student(self):

        print("\nYou can \"exit\", or \"restart\"")
        time.sleep(1)

        while True:

            fields = []

            fields.append(input("\nStudent First Name.....  "))

            if fields[-1] == "exit" or fields[-1] == "Exit":
                break

            elif fields[-1] == "restart" or fields[-1] == "Restart":
                pass

            fields.append(input("\nStudent Last Name.....  "))

            if fields[-1] == "exit" or fields[-1] == "Exit":
                break

            elif fields[-1] == "restart" or fields[-1] == "Restart":
                pass

            else:

                student = create_student(fields[0], fields[1])

                add_student_to_classroom(student, self.data)

                temp_dict = self.data["student_list"][-1]
                temp_string = "\n%s %s, has been added to the class list." % (temp_dict["first_name"], temp_dict["last_name"])

                print(temp_string)

    def remove_student(self):

        def temp_func(first_name, last_name):
            for student in self.data["student_list"]:
                if student["first_name"] == fields[0] and student["last_name"] == fields[1]:

                    msg = "\n%s %s has been removed from the class list..." % (student["first_name"], student["last_name"])
                    print(msg)

                    remove_student_from_classroom(student, self.data)
                    return True

        while True:

            fields = []

            fields.append(input("\nStudent First Name.... "))
            fields.append(input("\nStudent Last Name.... "))

            if temp_func(fields[0], fields[1]) is True:
                break

    def add_assignment(self):

        while True:

            fields = []

            fields.append(input("\nName of the assignemnt...  "))

            if fields[-1] == "exit":
                break
            elif fields[-1] == "restart":
                pass

            fields.append(input("\nDue date...  "))

            if fields[-1] == "exit":
                break
            elif fields[-1] == "restart":
                pass

            fields.append(input("\nPoints the assignemnt is out of...  "))

            if fields[-1] == "exit":
                break
            elif fields[-1] == "restart":
                pass

            temp_assignnment = create_assignment(fields[0], fields[1], fields[2])

            self.data["assignment_list"].append(temp_assignnment)

            temp_assignment = create_assignment(fields[0], fields[1], 0)

            for student in self.data["student_list"]:

                student["assignment_list"].append(temp_assignment)

            else:
                break

    def add_student_mark(self):
        def temp_func(data, name):

            for assignment in data["assignment_list"]:

                if assignment["name"] == name:
                    return True

            else:
                return False

        fields = []
        i = 0

        fields.append(input("\nWhat is the name of the assignemnt...  "))

        for assignment in self.data["assignment_list"]:

            if assignment["name"] == fields[0]:
                break

            i += 1

        for student in self.data["student_list"]:

            boolean = temp_func(student, fields[0])

            if boolean is True:
                msg = "\n What did %s %s get on this assignemnt...  " % (student["first_name"], student["last_name"])

                if len(student["assignment_list"]) >= i:
                    print(student["assignment_list"])
                    print(i)
                    student["assignment_list"][i]["points"] = input(msg)

    def calculate_student_avg(self):
        def temp_func(first_name, last_name):
            """ A temp function used for breaking from a nested for loop, within a while loop

            Args:
                -fist_name
                -second_name

            Returns:
                boolean for breaking
                """

            for student in self.data["student_list"]:

                    if first_name == student["first_name"] and last_name == student["last_name"]:
                        msg = "\nRyan has a %s percent average" % (calculate_average_mark(student, self.data) * 100)
                        print(msg)
                        return True

        while True:

            # If the user cannot pick a student, because non exist, break from the loop
            if self.data["student_list"] == []:
                break

            fields = []
            print("\nTo leave this menu enter \"exit\".")

            fields.append(input("\nStudent First Name... "))

            # The user can enter a exit command to leave at any time.
            if fields[-1] == "exit" or fields[-1] == "exit":
                break

            fields.append(input("\nStudent Last Name... "))

            if fields[-1] == "exit" or fields[-1] == "leave":
                break

            # To check for student existance, a nested for loop prevents breaking from inside the second layer
            if temp_func(fields[0], fields[1]) is True:
                break

            else:
                print("\nStudent not found, please try again....")

    def edit_student_info(self):
        """Edits a specified student's info using key/value input pairs
        Args:
            -None
        """
        fields = []

        fields.append(input("\nStudent First name...  "))
        fields.append(input("\nStudent Last name...  "))

        while True:

            key_word = input("\nWhat about the student are you altering? first_name? Or last_name...  ")
            value = input("\nWhat do you want it to be changed too...  ")

            for i in range(len(self.data["student_list"])):

                if self.data["student_list"][i]["first_name"] == fields[0] and self.data["student_list"][i]["last_name"] == fields[1]:
                    edit_student(self.data["student_list"][i], {key_word: value})

                    break

            else:
                print("\nInvalid Student key try \"first_name\", or \"last_name\"...")

            break

    def show_assignemnts(self):
        """Prints all assignments within the self.data["assignment_list"] var."""

        if self.data["assignment_list"] == []:

            print("\nNo assignments have been given...")

        for assignment in self.data["assignment_list"]:
            msg = "\n-%s, due on %s, out of %s..." % (assignment["name"], assignment["due"], assignment["points"])

            print(msg)

    def show_students(self):
        """Prints every student within the present student list (self.data["student_list"])"""

        if self.data["student_list"] == []:
            print("\n- No students... ")

        else:

            for student in self.data["student_list"]:

                msg = "\n-%s %s" % (student["first_name"], student["last_name"])

                print(msg)

    def update(self, cmd):
        """Used to route the general input stream into the user_interface_center
        Args:
            -user command -> cmd

        Returns:
            -None
        """

        if cmd == "help":
            self.help()

        elif cmd == "add-student":
            self.add_student()

        elif cmd == "remove-student":
            self.remove_student()

        elif cmd == "add-assignment":
            self.add_assignment()

        elif cmd == "calculate-student-avg":
            self.calculate_student_avg()

        elif cmd == "edit-student-info":
            self.edit_student_info()

        elif cmd == "add-student-mark":
            self.add_student_mark()

        elif cmd == "save":
            save_classroom_data(self.filename, self.data)

        elif cmd == "show-students":
            self.show_students()

        elif cmd == "show-assignment":
            self.show_assignemnts()

        elif cmd == "clear":
            clear()
        else:
            print("\nUnknown command..... ")
            self.help()
