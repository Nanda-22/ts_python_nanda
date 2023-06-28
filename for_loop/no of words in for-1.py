str="My name is Sai"
word_cnt=0
cnt=0
for i in str:
    print(i)
    cnt=cnt+1
    if i==" ":
        word_cnt=word_cnt+1
if cnt>=0:
    word_cnt=word_cnt+1    
print("Number of characters in the string without using len function",cnt)
print("Number of words",word_cnt)

