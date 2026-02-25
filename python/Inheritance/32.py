class Parent:
    def __init__(self):
        print("Parent Constructor")

    def __del__(self):
        print("Parent Destructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

    def __del__(self):
        print("Child Destructor")
        super().__del__()
# Create and delete object
c = Child()
del c
