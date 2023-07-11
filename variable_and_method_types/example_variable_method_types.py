#example progarm to count number of objects/students present in a given class
class student:
    count=0    # class variable or static variable 
    def __init__(self,sno,sname,location):  # it is constructor ... 
        print(self)
        student.count+=1
        self.rno=sno
        self.sname=sname
        self.location=location
    def display(self):        # instant Method
        print("Roll Number is",self.rno)
        print("Name is",self.sname)
        print("Location is ",self.location)
        x= self.rno + self.sname
        print("Rno and Sname is",x)

    def __del__(self): # destructors 
        student.count-=1
        print("No of Objects present in student class",student.count)
        


S1=student("1","Sai","Hyd")
print("Adress of S1",hex(id(S1)))
print("No of Objects for student class",S1.count)
print("No of Objects for student class",student.count)
S1.display()
print("Roll Number is",S1.rno)
print("Name is",S1.sname)
print("Location is ",S1.location)
print("No of Objects for student class",student.count)
S2=student("2","Ram","Chennai")
print("Address of S2",hex(id(S2)))
print("No of Objects for student class",S2.count)
print("No of Objects for student class",student.count)
print("No of Objects for student class",student.count)
S2.display()
del S1
del S2
