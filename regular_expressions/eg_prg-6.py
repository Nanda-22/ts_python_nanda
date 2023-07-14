#program for Extracting numbers from a string:

import re

pattern = r'\d+'
string = 'The recipe requires 2 cups of flour and 3 eggs.'

matches = re.findall(pattern, string)
print(matches)  
