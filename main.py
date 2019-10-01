from data_managment_methods import initialize_session
from user_interface_center import user_interface_controller

session_data, filename = initialize_session()

usr_interface = user_interface_controller(session_data, filename)

msg = "\nNow interacting with %s, enter \"help\" for the list of commands" % (session_data["course_code"])

print(msg)

while True:

    user_input = input("\n")

    user_input.lower()

    if user_input == "exit":
        usr_interface.update("save")
        break

    usr_interface.update(user_input)
