#program for the sum of the given numbers using tuple in functions
def Read_tuple_values():
    print("Enter how many elements in the tuple you want")
    n=int(input("Enter value "))
    l=[]
    for i in range(n):
        l.append(int(input("Enter {} value ".format(i))))

    t=tuple(l)
    return (l)


def sum_tuple(t):
    s=0
    for i in t:
        s=s+i
    return s

tuple_items=Read_tuple_values()
sum_of_tuple_items=sum_tuple(tuple_items)
print("Sum of tuple items is",sum_of_tuple_items)


      
