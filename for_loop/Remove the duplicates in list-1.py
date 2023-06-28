list1=[23,34,45,23,67,45,89,23]
result_list=[]
for i in list1:
    print(i)
    if i not in result_list:
        result_list.append(i)

print("Result list is",result_list)

result=list(set(list1))
print("Result list is",result)

