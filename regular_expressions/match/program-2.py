#match (): We can use match function to check the given pattern at beginning of target string.
import re
s=input("Enter string :")
p=input("Enter pattern to check:")
m=re.match(p,s)
if m!= None:
 print("Match is available at the beginningof the String")
 print("Start Index:",m.start(), "and EndIndex:",m.end(), " and Group is",m.group())
else:
 print("Match is not available at the beginning of the String")

print(m)
