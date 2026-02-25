#Example 4: Passing Arguments to Base Constructor

class Parent:
    def __init__(self, name):
        print("Parent Constructor: ", name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # passing argument to base
        print("Child Constructor: ", age)

obj = Child("sai", 25)
