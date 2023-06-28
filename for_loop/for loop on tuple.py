tuple1=(10,20,30,40,50)
cnt=0
max=tuple1[0]
min=tuple1[0]
sum=0
for each_item in tuple1:
    print(each_item)
    cnt=cnt+1
    sum=sum+each_item
    if max<=each_item:
        max=each_item
    if min>=each_item:
        min=each_item
    
print("Number of items in tuple ",cnt)
print("Max tuple element is",max)
print("Min tuple element is",min)
print("Sum of tuple elements is",sum)
