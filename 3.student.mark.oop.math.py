import math


class info: 
    def __init__(self,id,name):
        self.__id = id
        self.__name = name

    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def setName(self,name):
        self.__name = name
    def getInfo(self):
        print(f"ID: {self.__id}, Name: {self.__name}")

class Student(info):
    def __init__(self,id,name,dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
    
    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getDOB(self):
        return self.__dob
    
  

class Course(info):
    def __init__(self,id,name,credit):
        self.__id = id
        self.__name = name
        self.__credit = credit

    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getCredit(self):
        return self.__credit
    

class SchoolManagement(Course,Student):
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    
    def input_student(self):
        n = int(input("Enter number of students:"))
        for i in range(n):
            print(f"Enter the student {i+1} information:")
            id = input("Student ID:")
            name = input("Student Name:")
            dob = input("DOB:")
            #create a student obj to collect all information
            student = Student(id,name,dob)
            # append student to the list
            self.students.append(student)

    
                

    def list_students(self):
        for student in self.students:
            print(f"Student ID: {student.getID()}, Student Name: {student.getName()}, DOB: {student.getDOB()}")
    
    def input_course(self):
        n = int(input("Enter number of courses:"))
        for i in range(n):
            print(f"Input information of course {i+ 1}:")
            id = input("Course ID:")
            name = input("Course Name:")
            credit = input("Credit:")
            course = Course(id,name,credit)
            self.courses.append(course)
    
    def list_courses(self):
        # print(course_info)
        for course in self.courses:
            print(f"Course ID: {course.getID()}, Course Name: {course.getName()}, Course Credit: {course.getCredit()}")
            
    def input_student_marks(self,course_id):
        student_marks = {}
        print(f"Enter mark for course {course_id}")
        for student in self.students:
            mark =  float(input(f"Enter mark for student {student.getID()}:"))
            #value associated with this key is set to mark
            student_marks[student.getID()] = mark
        self.marks[course_id] = student_marks

        
    def list_student_marks(self,course_id):
        print(f"Mark for course {course_id}:")
        for student_id,mark in self.marks[course_id].items():
            for student in self.students:
                if student.getID() == student_id:
                    print(f"Student ID: {student.getID()}, Student Name: {student.getName()}, Mark: {mark}")
                    break

    def getCreditfromCourseID(self,courseID):
            for i in self.courses:
                if i.getID() == courseID:
                    return int(i.getCredit())

    def calculate_gpa(self,student_id):
        total_score = 0
        total_credit = 0
        for course_id in self.marks:
            for i in self.marks[course_id]:
                if i == student_id:
                    total_score += self.marks[course_id][i] * self.getCreditfromCourseID(course_id)
                    total_credit += self.getCreditfromCourseID(course_id)
        return math.floor((total_score/total_credit)*10)/10


def main():
    sm = SchoolManagement()

    while True:
        print("""
    1. Input student information
    2. Input course information
    3. Input mark for course
    4. List course
    5. List student
    6. List student mark for a course
    7. Calculate GPA
    8. Exit
              """)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            sm.input_student()

        elif choice == 2:
            sm.input_course()

        elif choice == 3:
            course_id = input("Enter course ID:")
            for course in sm.courses:
                if course.getID() != course_id:
                    print("Course not found!")
                    break
            sm.input_student_marks(course_id)

        elif choice == 4:
            lenCourse = len(sm.courses)
            if lenCourse == 0:
                print("No Course. Enter Course infomation first!")
                continue
            else:
                sm.list_courses()

        elif choice == 5:
            lenStudent = len(sm.students)
            if lenStudent == 0:
                print("No Student. Enter Student infomation first!")
                continue
            else:
                sm.list_students()

        elif choice == 6:
            course_id = input("Enter course ID: ")
            sm.list_student_marks(course_id)

        elif choice == 7:
            student_id = input("Enter student ID:")
            print(f"GPA of student {student_id}: {sm.calculate_gpa(student_id):.2f}")

        elif choice == 8:
            print("Exit program!")
            break

        else:
            print("Invalid choice. Enter again!")
            continue

if __name__ == "__main__":
    main()

    