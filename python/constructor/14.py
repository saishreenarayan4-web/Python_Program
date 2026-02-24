class Test:
    def __init__(self,msg):
        self.msg=msg
        print("constructor",self.msg)
    def __del__(self):
        print("destructor",self.msg)
def show():
    t1=Test("second")

t=Test("first")
show()
t2=Test("third")