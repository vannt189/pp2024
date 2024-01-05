#Input function

#input number of students
def setNumberOfStudent():
    num = int(input("Enter number of students: "))
    if (num < 0):
        print("Invalid number. Enter again!")
        return setNumberOfStudent()
    else:
        return num
    

#input student information

def setStudentInfo():
    SId = input("Enter student's ID: ")
    SName = input("Enter student's name: ")
    SDob = input("Enter student's D.O.B (dd/mm/yyyy): ")

    return {"Student ID":SId,"Student name":SName,"D.O.B": SDob}
    


#input number of course

def setNumberOfCourse():
    num = int(input("Enter number of courses: "))
    if (num < 0):
        print("Invalid number. Enter again!")
        return setNumberOfCourse()
    else:
        return num
    
#input course information:
    
def setCourseInfo():
    CId = input("Enter course's ID: ")
    CName = input("Enter course's name: ")
    return {"Course ID":CId,"Course Name":CName }

#select a course, input marks for student in this course

def setMarkCourse(course):
    mark_dict = {}

    for student in Info["Students"]:
        while True:
            try:
                mark = round(float(input(f"Enter mark for student {student['Student ID']}, course {course['Course Name']}: ")), 2)
                if mark < 0 or mark > 20:
                    print("Invalid mark. Enter again!")
                else:
                    mark_dict[student['Student ID']] = mark
                    break  
            except ValueError:
                print("Invalid input. Enter a valid mark!")

    course['Mark'] = mark_dict

#Listing function 
    
#list students

def listStudents():
    print("List of students: ")
    for student in Info["Students"]:
        print(f"ID: {student['Student ID']}, Name: {student['Student name']}, D.O.B: {student['D.O.B']}")

#list course
        
def listCourses():
    print("List of courses: ")
    for course in Info["Courses"]:
        print(f"ID: {course['Course ID']}, Name: {course['Course Name']}")
    
#show student marks for a given course

def listMark(courseID):
    print(f"List of marks for course {courseID}: ")
    for course in Info["Courses"]:
        if course['Course ID'] == courseID:
            for studentID in course['Mark']:
                print(f"Student ID: {studentID}, Mark: {course['Mark'][studentID]}")
        else:
            print("Invalid course ID. Enter again!")
            

    
Info = {
    "Students": [],
    "Courses": [],
}

#main function 

def main():

    while True:
        print("""
    1. Input student information
    2. Input course information
    3. Input mark for course
    4. List student
    5. List course
    6. List mark
    7. Exit
              """)
        choice = input("Enter your choice: ")
        if choice == "1":
            numOfStudent = setNumberOfStudent()
            for i in range(numOfStudent):
                student = setStudentInfo()
                Info["Students"].append(student)

        elif choice == "2":
            numOfCourse = setNumberOfCourse()
            for i in range(numOfCourse):
                course = setCourseInfo()
                setMarkCourse(course)
                Info["Courses"].append(course)

        elif choice == "3":
            courseID = input("Enter course ID: ")
            listMark(courseID)

        elif choice == "4":
            lenStudent = len(Info["Students"])
            if lenStudent == 0:
                print("No student. Enter Students information first!")
                continue
            else:
             listStudents()

        elif choice == "5":
            lenCourse = len(Info['Courses'])
            if lenCourse == 0:
                print("No Course. Enter Course infomation first!")
                continue
            else:
                listCourses()

        elif choice == "6":
            courseID = input("Enter course ID: ")
            listMark(courseID)

        elif choice == "7":
            break

        else:
            print("Invalid choice. Enter again!")
            continue

if __name__ =="__main__":
    main()