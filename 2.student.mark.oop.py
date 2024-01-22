class Student:
    def __init__(self, id,name,dob):
        self.id = id
        self.name = name
        self.dob = dob
    
    def newStudent(self,id,name,dob):
        obj = Student(id,name,dob)
        ls.append(obj)

    def display(self,obj):
        print("Id: ", obj.id)
        print("Name: ", obj.name)
        print("Dob: ", obj.dob)
        print("\n")

    def searchStudent(self,id):
        for i in range(ls.__len__()):
            if(ls[i].id == id):
                return i
            
    def deleteStudent(self,id):
        i = obj.searchStudent(id)
        del ls[i]

class Course: 

    def __init__(self,courseID,courseName):
        self.courseID = courseID
        self.courseName = courseName

    def newCourse(self,id,name):
        obj = Course(id,name)
        coursels.append(obj)

    def display(self,obj):
        print("Id: ", obj.courseID)
        print("Name: ", obj.courseName)
        print("\n")




ls = []
coursels = []

#Object for Student class 
obj = Student(0,'','')
obj.newStudent(1,'A','1/1/2000')
obj.newStudent(2,'B','1/2/2000')
obj.newStudent(3,'C','3/3/2003')

#Object for Course class
obj2 = Course(0,'')
obj2.newCourse(1,'ADS')
obj2.newCourse(2,'Python')
obj2.newCourse(3,'OOP')

#print list of Student and Course
print("List of Student: ")
for i in range(ls.__len__()):
    obj.display(ls[i])

print("List of Courses: ")
for i in range(coursels.__len__()):
    obj2.display(coursels[i])