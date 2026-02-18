student = {}
n = int(input("Enter number of students"))
for i in range(n):
    print("Enter details for student",i + 1)
    roll = int(input("Enter roll number"))
    name = input("Enter name")
    age = int(input("Enter age"))
    course = input("Enter course")
    student[roll] = {
    "name": name,
    "age": age,
    "course": course
    }

print("Student details")
print(student)


