#fullmatch (): We can use fullmatch () function to match a pattern to all of target string
import re
p="hyderabad"
m=re.fullmatch(p,"hyderabad")
if m!= None:
 print("Match is available at the beginningof the String")
 print("Start Index:",m.start(), "and EndIndex:",m.end(), " and Group is",m.group())
else:
 print("Match is not available at the beginning of the String")

print(m)
