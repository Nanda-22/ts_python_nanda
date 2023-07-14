#Character classes:  We can use character classes to search a group of characters
#by using Character classes we can define by all followimg ways
import re
count=0
print("String length is",len("a7Sb@k9#Az"))
"""match=re.finditer("[abc]","a7Sb@k9#Az")
match=re.finditer("[^abc]","a7Sb@k9#Az")
match=re.finditer("[a-z]","a7Sb@k9#Az")
match=re.finditer("[A-Z]","a7Sb@k9#Az")
match=re.finditer("[0-9]","a7Sb@k9#Az")
match=re.finditer("[a-zA-Z]","a7Sb@k9#Az")
match=re.finditer("[a-zA-Z0-9]","a7Sb@k9#Az")"""
match=re.finditer("[^a-zA-Z0-9]","a7Sb@k9#Az")
for m in match:
 count+=1
 print(m.start(),"......",m.group())

print("Number of Matches",count)
