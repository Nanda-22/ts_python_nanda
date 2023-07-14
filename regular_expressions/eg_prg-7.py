#program for Extracting all numbers from a string:
import re

pattern = r'\d{1,10}'
"""pattern = r'\d*'
pattern = r'\d+'
pattern = r'\d?'"""

string = "we have 123 cars and 355 bikes"

matches = re.findall(pattern, string)
print(matches) 
