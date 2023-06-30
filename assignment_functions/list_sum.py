#program for the sum of the given numbers using sum in functions
def Read_list_values():
    print("Enter how many elements in the list you want")
    n=int(input("Enter value  "))
    l=[]
    for i in range(n):
        l.append(int(input("Enter {} value ".format(i))))

    return (l)

def sum_list(l):
    s=0
    for i in l:
        s=s+i
    return s
    
list_items=Read_list_values()
sum_of_list_items=sum_list(list_items)
print("Sum of list items is",sum_of_list_items)

