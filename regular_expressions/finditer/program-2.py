#finditer(): Returns an Iterator object which , Match object for every Matchimport re
import re
pattern = r'Python'
string = 'Python is a scripting language. Python is mainly used in Automation. Python is easy to learn'
count=0
matches = re.finditer(pattern, string)

for match in matches:
    # Access match object properties
    print('Match found:', match.group())
    print('Starting index:', match.start())
    print('Ending index:', match.end())
    count+=1

print("Number of occurances",count)
