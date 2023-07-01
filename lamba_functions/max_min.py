#Lambda Functions

def max(a,b):
    if a>b:
        return a
    else:
        return b

x=10
y=20
print("Max of {} and {} is {} ".format(x,y,max(x,y)))

f=lambda x,y : x if x>y else y
print(f(10,20))
