#Pre-defined Character classes:
#by using Pre-defined Character classes we can define by all followimg ways
import re
print("Actual String length ",len("a7Sb @k 9#Az"))
count=0
match=re.finditer("\s","a7Sb @k 9#Az")
"""match=re.finditer("\S","a7Sb @k 9#Az")
match=re.finditer("\d","a7Sb @k 9#Az")
match=re.finditer("\D","a7Sb @k 9#Az")
match=re.finditer("\w","a7Sb @k 9#Az")
match=re.finditer("\W","a7Sb @k 9#Az")
match=re.finditer(".","a7Sb @k 9#Az")"""
for m in match:
 count+=1
 print(m.start(),"......",m.group())

print("Number of Matches",count)
