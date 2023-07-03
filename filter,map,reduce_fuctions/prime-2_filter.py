#Filter Method
#test customized filter method ... it is filtering the only prime numbers from list of numbers

def is_prime(x):
    fact_cnt=0
    for i in range(1,x+1):
        if x%i==0:
            fact_cnt+=1
    if fact_cnt==2:
        return True
    else:
        return False
    
def test(prime_test,x):
    for i in x:
        if prime_test(i):
            print("{} is Prime".format(i))
        
test_list=list(range(1,101))
test(is_prime,test_list)
