#compile () : This function is used to compile a pattern into Regex Object
import re
count=0
pattern=re.compile("AB")
match=pattern.finditer("abaababa")
for m in match:
 count+=1
 print(m.start(),"...",m.end(),"...",m.group())

 
print("The number of occurrences: ",count)
