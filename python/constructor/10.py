class Test:
    def __init__(self):
        self.__b = 20
    
    def get_b(self):
        return self.__b

t = Test()
print(t.get_b())
