#program for the sum of the given numbers using set in functions
def Read_set_values():
    print("Enter how many elements in the set you want")
    n=int(input("Enter value "))
    l=[]
    for i in range(n):
        l.append(int(input("Enter {} value ".format(i))))

    s=set(l)
    return (l)

def sum_set(s):
    S=0
    for i in s:
        S=S+i
    return S

set_items=Read_set_values()
sum_of_set_items=sum_set(set_items)
print("sum of set items is",sum_of_set_items)


      
