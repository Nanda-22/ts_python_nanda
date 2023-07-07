#exception handling
from math import sqrt 
try:
    l=[10,2]
    b=sqrt(l[1]) 
    print("sqrt is",b) 
    b=l[0]/l[1]
    print("Division is",b)
except ZeroDivisionError as e:
    print("Divisor not to be a zero",e)
except NameError as e:
    print("Name Error message is",e)
except ValueError as e:
    print("Value Error message is",e)
except IndexError as e:
    print("Index Error message is",e)
except Exception as e:
    print("Generic Exception",e)
else:
    print("\n there are no exception")
    
finally:
     print("\n Finally block will execute Irespective the exception")


print("a value is",l)
print("Welcome to python world")
