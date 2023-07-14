#program for Spliting the given string 
import re

pattern = r'\s+'
string = 'Hello     World   Python'

tokens = re.split(pattern, string)
print(tokens)
