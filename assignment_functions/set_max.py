#program for the max of the given numbers using set in functions
def Read_set_values():
    print("Enter how many elements in the set you want")
    n=int(input("Enter value "))
    l=[]
    for i in range(n):
        l.append(int(input("Enter {} value ".format(i))))

    s=set(l)
    return (l)

def max_set(s):
    max=s[0]
    for i in s:
        if max<i:
            max=i
    return max


set_items=Read_set_values()
max_of_set_items=max_set(set_items)
print("max of set items is",max_of_set_items)


      
