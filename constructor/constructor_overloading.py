#example program for constructor_overloading
class student:
    count=0
    def __init__(self,sno,sname,location):
        student.count+=1
        self.rno=sno
        self.sname=sname
        self.location=location
    def display(self):
        print("Roll Number is:",self.rno)
        print("Name is:",self.sname)
        print("Location is:",self.location)

s1=student("1","sai","hyd")
print("Address of s1",id(s1))
s2=student("2","Ram","chennai")
print("Address of s2",id(s2))      
s1.display()
s2.display()
