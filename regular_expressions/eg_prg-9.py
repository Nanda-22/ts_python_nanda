#program by using or in the pattern and getting required output
import re

pattern = r'(apple|banana)'
string = 'I have an apple and a banana.'
matches = re.findall(pattern, string)
print(matches)  
