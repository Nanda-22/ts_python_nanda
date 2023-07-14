#finditer(): Returns an Iterator object which , Match object for every Matchimport re
import re

pattern = r'dog'
string = 'dog is a pet animal.now a days people are liking dogs very much'
count=0
matches = re.finditer(pattern, string)

for match in matches:
    # Access match object properties
    print('Match found:', match.group())
    print('Starting index:', match.start())
    print('Ending index:', match.end())
    count+=1

print("Number of occurances",count)
