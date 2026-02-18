student = {}
roll = int(input("Enter roll"))
name = input("Enter name")
age = int(input("Enter age"))
course = input("Enter course")
student[roll] = {
    "name": name,
    "age": age,
    "course": course
}
print("\nStudent Details")
print("Name:", student[roll]["name"])
print("Age:", student[roll]["age"])
print("Course:", student[roll]["course"])
