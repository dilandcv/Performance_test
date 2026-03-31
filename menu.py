from funtions import * #We import the functions
bd=[]
loop = True
print("============================")
print("==========WELCOME===========")
print("============================")

#menu to show the customer the options that can be performed
while loop:
    print("""
Choose an option:
1) Add student
2) Show students
3) Search student
4) Update student
5) Remove student 
6) Exit
""")
    try:
        option = int(input("Choose an option: "))

#This is where the client is asked for information about the student
        if option == 1:
            id = int(input("Insert the document number: "))
            name = input("Insert the student name : ")
            age = int(input("Insert the age: "))
            if age <= 0:
                print ("invalid age.try again")
                continue
            course = input("Insert the course/program: ")
            state = input("Is the student active or inactive?: ")
            print("\nStudent successfully added!")
            add_student(bd,id,name,age,course,state)

#we call the function show_students for show the students
        elif option == 2:
             show_student(bd)

#We ask for the name of the student whose information you want to see.
        elif option == 3:
            name = input("Insert name: ")
            student = search_student(bd, name)

            if student:
                print(student)
            else:
                print("Student not found")
#We request the student's new information and update the list with their information.
        elif option == 4:
            name = input("insert the student name: ")


            age = input("New age (Enter to skip): ")    
            course = input("New course(Enter to skip): ")
            state = input("Update state(Enter to skip): ")
            print ("Updated information!")
    
            update_student(
                bd,
                name,
                int(age) if age else None,
                str(course) if course else None,
                str(state) if state else None)
#The name of the student to be removed is requested and then deleted from the list.            
        elif option == 5:
            name = input("Insert the student name: ")
            
            remove_student(bd,name)
            print("Student removed successfully")
#option to exit the program          
        elif option == 6:
            loop = False
            print("Exiting program...")
            break
        
        else:
            print("Invalid option.try again")

    except:
        print("Invalid input.try again")




