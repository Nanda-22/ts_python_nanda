marks=[78,76,72,98,78,94]
sum=0
print("Max of marks",max(marks))
print("Min of marks",min(marks))

min=marks[0]
max=marks[0]
cnt=0
for i in marks:
    print(i)
    cnt=cnt+1
    sum=sum+i
    if i>=max:
        max=i
    if i<=min:
        min=i
print("Total marks",sum)
print("Max marks",max)
print("Min marks",min)
print("Number of items in the list",cnt)
print("Average Marks is",sum/cnt)
