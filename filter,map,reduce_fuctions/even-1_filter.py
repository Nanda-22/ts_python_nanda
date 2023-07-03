#Filter Method
#With Lambda Dunction

test_list=list(range(1,101))
even_list_100=list(filter(lambda x:x%2==0,test_list))
print("Even Numbers from 1 to 100 are",even_list_100)
