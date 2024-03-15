#Input function
students = []
courses = []
marks = {}


def input_student_info():
    n = int(input("Enter number of student:"))
    for i in range(n):
        student = {}
        print(f"Enter student {i+1} information:")
        student["id"] = input("Enter student's ID:")
        student["name"] = input("Enter student's name:")
        student["dob"] = input("Enter student's D.O.B (dd/mm/yyyy):")
        students.append(student)

def input_course_info():
    n = int(input("Enter number of course:"))
    for i in range(n):
        course = {}
        course["id"] = input("Enter course's ID:")
        course["name"] = input("Enter course's name:")
        courses.append(course)

def input_mark(course_id):
    student_marks = {}
    for student in students:
        mark = float(input(f"Enter mark for student {student["id"]} (Course ID: {course_id}):"))

        #student id is used as key in student_marks dict 
        student_marks[student["id"]] = mark
    # explain this part
    marks[course_id] = student_marks

def list_student():
    for student in students:
        print(f"Student ID: {student["id"]}, Student Name: {student["name"]},DOB: {student["dob"]}")
def list_course():
    for course in courses:
        print(f"Course ID: {course["id"]} - Course Name: {course["name"]}")

def list_mark(course_id):
    if course_id not in marks:
        print("Course not found!")
        return
    print(f"List of marks for course {course_id} :")
    #iterate through dict store under the course_id key in marks dict
    for student_id, mark in marks[course_id].items():
        #items(): return the key-value pairs of dict, use when loop though key-value simultaneously
        for student in students:
            #check if the current student matches the student from mark dict
            if student["id"] == student_id:
                print(f"Student ID: {student["id"]}, Mark: {mark}")
                break



def main():

    while True:
        print("""
    1. Input student information
    2. Input course information
    3. Input mark for course
    4. List course
    5. List student
    6. List student mark for a course
    7. Exit
              """)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            input_student_info()

        elif choice == 2:
            input_course_info()

        elif choice == 3:
            course_id = input("Enter course ID: ")
            input_mark(course_id)

        elif choice == 4:
            lenCourse = len(courses)
            if lenCourse == 0:
                print("No Course. Enter Course infomation first!")
                continue
            else:
                list_course()

        elif choice == 5:
            lenStudent = len(students)
            if lenStudent == 0:
                print("No Student. Enter Student infomation first!")
                continue
            else:
                list_student()

        elif choice == 6:
            course_id = input("Enter course ID: ")
            list_mark(course_id)

        elif choice == "7":
            print("Exit program!")
            break

        else:
            print("Invalid choice. Enter again!")
            continue

if __name__ =="__main__":
    main()