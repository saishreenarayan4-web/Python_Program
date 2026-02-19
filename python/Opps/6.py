class Student:
    clg="iter"
    def __init__(self):   # constructor   but in java and c++ constructor same as classname
        self.name="muna" # instance variable  object data 
        self.rollno=1
s=Student() # object create  got where constrcutor 

print(s.__dict__)  
print(Student.__dict__)
print("my name=",s.name)
print("my rollno=",s.rollno)
print("clg name=",s.clg)
print("clg name better way =",Student.clg)
#print("my name=",Student.name)  error name is part of object 

