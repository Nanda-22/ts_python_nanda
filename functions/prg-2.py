#function without parameter and no return type

def Calculate():
    print("1- Add\n 2-Substraction \n 3-Prodcut \n 4- Division")
    op=eval(input("Enter your choice "))
    if op==1:
         x=eval(input("Enter a number "))
         y=eval(input("Enter a number "))
         print(f"Sum of {x} and {y} is {x+y}")
         
    elif op==2:
         x=eval(input("Enter a number "))
         y=eval(input("Enter a number "))
         print(f"Substtraction of {x} and {y} is {x-y}")
    elif op==3:
         x=eval(input("Enter a number"))
         y=eval(input("Enter a number "))
         print(f"Product of {x} and {y} is {x*y}")
    elif op==4:
         x=eval(input("Enter a number "))
         y=eval(input("Enter a number "))
         print(f"Division of {x} and {y} is {x/y}")
    else:
        print("\n Invalid Operation")

Calculate()
