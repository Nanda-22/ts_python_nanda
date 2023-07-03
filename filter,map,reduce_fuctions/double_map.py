#Map ()
#Without Lambda 

def double_number(x):
    return 2*x

mylist=[1,2,3,4,5,6]
double_list=list(map(double_number,mylist))
print("After Doubling",double_list)
