#Filter Method

def is_prime(x):
    fact_cnt=0
    for i in range(1,x+1):
        if x%i==0:
            fact_cnt+=1
    if fact_cnt==2:
        return True
    else:
        return False


test_list=list(range(1,101))

prime_list_100=list(filter(is_prime,test_list))
print(prime_list_100)
