import math
def list_courses(self):
        # print(course_info)
        for course in self.courses:
            print(f"Course ID: {course.getID()}, Course Name: {course.getName()}, Course Credit: {course.getCredit()}")

def list_student_marks(self,course_id):
        print(f"Mark for course {course_id}:")
        for student_id,mark in self.marks[course_id].items():
            for student in self.students:
                if student.getID() == student_id:
                    print(f"Student ID: {student.getID()}, Student Name: {student.getName()}, Mark: {mark}")
                    break

def calculate_gpa(self,student_id):
        total_score = 0
        total_credit = 0
        for course_id in self.marks:
            for i in self.marks[course_id]:
                if i == student_id:
                    total_score += self.marks[course_id][i] * self.getCreditfromCourseID(course_id)
                    total_credit += self.getCreditfromCourseID(course_id)
        return math.floor((total_score/total_credit)*10)/10
