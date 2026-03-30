from funtions import *
bd=[]
loop = True

print("========")
print("WELCOME")
print("========")

while loop:
    print("""
choose an option:
1) Add student
2) show students
3)search student
4) update student
5) remove student 
6) exit
""")
    try:
        option = int(input("choose an option: "))

        if option == 1:
            name = input("insert the student name : ")
            while age < 0:
                age = int(input("insert the age: "))
            course = input("insert the course/program: ")
            state = input("is the student active or inactive?: ")
            print("student successfully added")
            add_student(bd,name,age,course,state)


        elif option == 2:
             show_student(bd)

        elif option == 3:
            name = input("insert the student name: ")
            student = search_student(bd,name)

            if student:
                print(student)
            else: 
                print("student not found")

        elif option == 4:
            name = input("insert the student name : ")

            age = input("new age (enter to skip): ")
            course = input("new course(enter to skip): ")
            state = input("update state(enter to skip): ")
            print ("Updated information")

            update_student(bd,name,
                           int(age) if age else None)
            
        elif option == 5:
            name=input("insert the student name : ")
            remove_student(bd,name)
            print("Student removed successfully")

        elif option == 6:
            loop = False
            break
        
        else:
            print("invalid option.try again")

    except:
        print("invalid input.try again")




