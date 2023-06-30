#program for the min of the given numbers using set in functions
def Read_set_values():
    print("Enter how many elements in the set you want")
    n=int(input("Enter value "))
    l=[]
    for i in range(n):
        l.append(int(input("Enter {} value ".format(i))))

    s=set(l)
    return (l)

def min_set(s):
    min=s[0]
    for i in s:
        if min>i:
            min=i
    return min


set_items=Read_set_values()
min_of_set_items=min_set(set_items)
print("min of set items is",min_of_set_items)


      
