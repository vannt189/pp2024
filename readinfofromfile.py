import json
f = open("student.info.txt")
student_info = []
for line in f.readlines():
    data = line.split()
    student_info.append(data)

print(student_info)

f.close()

g = open("course.info.txt")
course_info = []
for line in g.readlines():
    data = line.split()
    course_info.append(data)
print(course_info)
g.close()

m = open("mark.json")
mark_info = json.load(m)
print(mark_info)
    