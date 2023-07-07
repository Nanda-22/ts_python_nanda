#program for divison using exception handling 
try:
 a = int(input("Enter Num1:"))
 b = int(input("Enter Num2:"))
 print("result is:", a / b)
except Exception as msg:
 print(msg)
