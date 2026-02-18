student = {}
for i in range(2):
    roll = int(input("Enter roll: "))
    name = str(input("Enter name: "))
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    student[roll] = {
        "name": name,
        "age": age,
        "course": course
    }

print(student)
