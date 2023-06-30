#function without arguements and return type
def Read_values():
    a= eval(input("Enter a number "))
    b= eval(input("Enter a number "))
    return (a,b)

t= Read_values()
print(type(t))
print(t[0])
print(t[1])

(x,y)=Read_values()

print("x=",x)
print("y=",y)



def Read_values():
    a= eval(input("Enter a number "))
    b= eval(input("Enter a number "))
    return (a,b)

def max(x,y):
    if x>y:
        return x
    else:
        return y

t= Read_values()

max_value=max(t[0],t[1])

print("max of {} and {} is {}".format(t[0],t[1],max_value))
