Student = dict() # creates an empty dictionary

start = True

while start:
    
    F_name = input("Student First Name: ")
    L_name = input ("Stuendt Last Name: ")
    
    Student[F_name] = L_name

    print (Student[F_name]) #returns the value

    
    ask = input("Do you want to continue (Y/N)")

    if ask == "Y":
        continue
    else: 
        start = False

print (Student) #returns the dictionary 

