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

def input_course(self):
        n = int(input("Enter number of courses:"))
        for i in range(n):
            print(f"Input information of course {i+ 1}:")
            id = input("Course ID:")
            name = input("Course Name:")
            credit = input("Credit:")
            course = Course(id,name,credit)
            self.courses.append(course)

def input_student_marks(self,course_id):
        student_marks = {}
        print(f"Enter mark for course {course_id}")
        for student in self.students:
            mark =  float(input(f"Enter mark for student {student.getID()}:"))
            #value associated with this key is set to mark
            student_marks[student.getID()] = mark
        self.marks[course_id] = student_marks