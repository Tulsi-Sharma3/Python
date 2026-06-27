class Student:

    name = "anonymous"
    def __init__(self,name):
        self.name = name

    def hello(self):
        print("Hello")

s1 = Student("Rohan")
print(s1.name)
print(s1.hello())
