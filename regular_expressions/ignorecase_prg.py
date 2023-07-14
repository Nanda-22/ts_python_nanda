#IGNORECASE(): it will ignore the given string is upper/lower case
import re

pattern = r'apple'
string = 'I have an APPLE and a banana.'
matches = re.findall(pattern, string,re.IGNORECASE)
print(matches) 
