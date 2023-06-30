#program for the min of the given numbers using tuple in functions
def Read_tuple_values():
    print("Enter how many elements in the tuple you want")
    n=int(input("Enter value "))
    l=[]
    for i in range(n):
        l.append(int(input("Enter {} value ".format(i))))

    t=tuple(l)
    return (l)

def min_tuple(t):
    min=t[0]
    for i in t:
        if min>i:
            min=i
    return min


tuple_items=Read_tuple_values()
min_of_tuple_items=min_tuple(tuple_items)
print("min of tuple items is",min_of_tuple_items)


      
