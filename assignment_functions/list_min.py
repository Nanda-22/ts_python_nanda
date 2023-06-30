#program for the min of the given numbers using sum in functions
def Read_list_values():
    print("Enter how many elements in the list you want")
    n=int(input("Enter value "))
    l=[]
    for i in range(n):
        l.append(int(input("Enter {} value ".format(i))))

    return (l)

def min_list(l):
    min=l[0]
    for i in l:
        if min>i:
            min=i
    return min


list_items=Read_list_values()
min_of_list_items=min_list(list_items)
print("Min of list items is",min_of_list_items)
