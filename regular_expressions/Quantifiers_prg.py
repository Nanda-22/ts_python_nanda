#Quantifiers: We can use quantifiers to specify the number of occurrences to match.
#by using Quantifiers we can define by all followimg ways
import re
match=re.finditer("a","abaabaaab")
"""match=re.finditer("a+","abaabaaab")
match=re.finditer("a*","abaabaaab")
match=re.finditer("a?","abaabaaab")
match=re.finditer("a{2}","abaabaaab")
match=re.finditer("a{2,3}","abaabaaab")"""
for m in match:
 print(m.start(),"......",m.group())
