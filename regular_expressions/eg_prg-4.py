#program for Replacing the given string
import re

pattern = r'butter'
string = 'I love peanut butter on my toast.'

new_string = re.sub(pattern, 'jam', string)
print(new_string)
