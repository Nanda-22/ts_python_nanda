#Filter Method
#Without Lambda Dunction

test_list=list(range(1,101))
def is_even(num):
    if num%2==0:
        return True
    else:
        return False


even_list_100=list(filter(is_even,test_list))
print("Even Numbers from 1 to 100 are",even_list_100)
