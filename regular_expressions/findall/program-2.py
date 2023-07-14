#findall (): To find all occurrences of the match.
import re
p="bad"
matches=re.findall(p,"hyderabad is not a bad city")
if len(matches)>0:
    for m in matches:
     print(m)
else:
    print("pattern",p,"Not found")
