def add_student(bd,id,name,age,course,state): #function for save the students in the list(bd)
    student={"id":id,
             "name":name,
             "age":age,
             "course":course,
             "state":state}
    bd.append(student)
#function for show all the student saved in the list(bd)   
def show_student(bd):
    if not bd:
        print("data base is empty")
        return
    for student in bd:
        print(f"Student:{student["name"]}\nDocument number:{student["id"]}\nage:{student["age"]}\nCourse:{student["course"]}\nState:{student["state"]}")
        print ("=" * 32)
#function to search for only a specific student
def search_student(bd,name):
    for student in bd:
        if student["name"] == name:
            return student 
    return None  

#function to update some data of the student(s)   
def update_student(bd, name, new_age=None, new_course=None, new_state=None):
    student = search_student(bd,name)
#The new data is added to the old data.
    if student:
        if new_age is not None:
            student["age"] = new_age
        if new_course is not None:
            student["course"] = new_course 
        if new_state is not None:
            student["state"]= new_state
    else:
        print("student not found")
#function to remove a student from the "database"
def remove_student(bd, name):
    student = search_student(bd,name)

    if student:
        bd.remove(student)
    else:
        print("student not found")

                  