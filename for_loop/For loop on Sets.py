set1={45,65,23,12,78}
cnt=0
max=0
min=0
sum=0
for each_set_item in set1:
    print(each_set_item)
    cnt=cnt+1
    sum=sum+each_set_item
    if max<=each_set_item:
        max=each_set_item
    if min>=each_set_item:
        min=each_set_item
print("Number of items in set ",cnt)
print("Max set element is",max)
print("Min set element is",min)
print("Sum of set elements is",sum)
