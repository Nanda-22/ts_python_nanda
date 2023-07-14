#finditer(): Returns an Iterator object which , Match object for every Match
#using quantifiers
import re
match=re.finditer("a","abaabaaab")
#match=re.finditer("a+","abaabaaab")
#match=re.finditer("a*","abaabaaab")
#match=re.finditer("a?","abaabaaab")
#match=re.finditer("a{2}","abaabaaab")
#match=re.finditer("a{2,3}","abaabaaab")
for m in match:
 print(m.start(),"......",m.group())
