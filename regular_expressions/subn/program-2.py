#subn ():  It is exactly same as sub except it can also returns the number of replacements.
import re
s=re.subn("[0-9]","$","ne7f3tye429jr93")
print(s)

print("The Result String:",s[0])
print("The number of replacements:",s[1])
