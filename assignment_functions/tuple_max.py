#program for the max of the given numbers using tuple in functions
def Read_tuple_values():
    print("Enter how many elements in the tuple you want")
    n=int(input("Enter value "))
    l=[]
    for i in range(n):
        l.append(int(input("Enter {} value ".format(i))))

    t=tuple(l)
    return (l)


def max_tuple(t):
    max=t[0]
    for i in t:
        if max<i:
            max=i
    return max

tuple_items=Read_tuple_values()
max_of_tuple_items=max_tuple(tuple_items)
print("max of tuple items is",max_of_tuple_items)


      
