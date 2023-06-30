#program for the max of the given numbers using sum in functions
def Read_list_values():
    print("Enter how many elements in the list you want")
    n=int(input("Enter value  "))
    l=[]
    for i in range(n):
        l.append(int(input("Enter {} value ".format(i))))

    return (l)

def max_list(l):
    max=l[0]
    for i in l:
        if max<i:
            max=i
    return max

list_items=Read_list_values()
max_of_list_items=max_list(list_items)
print("Max of list items is",max_of_list_items)
