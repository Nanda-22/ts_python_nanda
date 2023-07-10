#data memebers and function memebers
class test:
    def read_data(self):
        test.a=eval(input("Enter a value "))
        test.b=eval(input("Enter b Value "))
    def print_data(self):
        print("A value is ",test.a)
        print("B value is ",test.b)
    def __init__(self):
        a=0
        b=0
        print("I am in constructor menthod")
        print("a=",a,"b=",b)
            
test_obj=test()
test_obj.read_data()
test_obj.print_data()
