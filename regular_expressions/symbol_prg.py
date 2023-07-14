#$ Symbol: We can use $ symbol to check whether the given target string ends with our provided pattern or not
import re
s="Learning Python is Very Easy"
#s="we are Learning Python"
m=re.search("Easy$",s)
if m != None:
 print("Target String ended with Easy")
else:
 print("Target String Not ended with Easy")
 
