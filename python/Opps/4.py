class Student:
    name="#"   #class variable   common for all object
    rollno=0   # class variable 
s=Student()
print(s.__dict__)  # { }
print(Student.__dict__)
print(s.name)
s.name="muna"
print(s.__dict__)
