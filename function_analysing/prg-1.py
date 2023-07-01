#Function Aliasing:
def f1():
 print("Hello")
f2=f1
f2()
print(id(f1))
print(id(f2))
