#subn ():  It is exactly same as sub except it can also returns the number of replacements.
import re
s=re.subn("[a-z]","#","a7b9c5k8z")
print(s)

print("The Result String:",s[0])
print("The number of replacements:",s[1])
