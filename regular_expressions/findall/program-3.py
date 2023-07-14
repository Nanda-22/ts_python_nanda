#findall (): To find all occurrences of the match.
import re
p=input("Enter pattern to check: ")
matches=re.findall(p,"hyderabad is good city")
if len(matches)>0:
    for m in matches:
     print(m)
else:
    print("pattern",p,"Not found")
