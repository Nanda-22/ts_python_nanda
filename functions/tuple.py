# Passing and Returning different data structures like tuple
def read_data_tuple():
    student=tuple()  
    print("\n Enter how many elements in the tuple")
    n=eval(input("Enter no of subjects "))
    for i in range(n):
        marks=int(input("Enter Marks "))
        student=student+(marks,)
    return (student)
   
def max_marks(s):
    max_mark=0
    for sub in s:
        if sub>max_mark:
            max_mark=sub
    return max_mark

def min_marks(s):
    min_mark=100
    for sub in s:
        if sub<min_mark:
            min_mark=sub
    return min_mark

def sum_marks(s):
    total_mark=0
    for sub in s:
            total_mark=total_mark+sub
    return total_mark

s=read_data_tuple()
print(s)

print("Max Mark marks is:",max_marks(s))
print("Min Mark marks is:",min_marks(s))
print("Total marks is:",sum_marks(s))
