#finditer(): Returns an Iterator object which , Match object for every Match
import re

pattern = r'your'
string = 'your_string_here'

matches = re.finditer(pattern, string)

for match in matches:
    # Access match object properties
    print('Match found:', match.group())
    print('Starting index:', match.start())
    print('Ending index:', match.end())
