#constructor/destructor
class test:
    def __init__(self,msg):
        self.msg=msg
        print("constructor",self.msg)
    def __del__(self):
        print("destructor",self.msg)
t=test("first")
t1=test("second")
del t
t2=test("third")