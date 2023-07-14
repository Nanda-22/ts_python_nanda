#search ():   We can use search () function to search the given pattern in the target string.
import re
p=input("Enter pattern to check: ")
m=re.search(p,"hyderabad")
if m!= None:
 print("Match is available")
 print("First Occurrence of match with start index:",m.start(),"and end index:",m.end())
else:
 print("Match is not available")
print(m)
