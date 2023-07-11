#example program using method types 
class Student:
    inst="durgasoft" 
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        print((self.m1+self.m2+self.m3)/3)
    @classmethod
    def m1(cls):
        print(cls.inst)
    @staticmethod
    def add(a,b):
        print("sum is:",a+b)
    @staticmethod
    def f1():
        print("Hello")
s1=Student(78,87,69)
s2=Student(90,86,94)
s1.avg()
s2.avg()
Student.m1()
s1.add(10,20)
s1.f1()
