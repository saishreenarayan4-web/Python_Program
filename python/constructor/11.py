class Test:
    def __init__(self):
        print("constructor")
    def __init__(self):
        print("destructor")
t = Test()
t1 = Test()
del t
t2 = Test()
