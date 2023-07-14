#program checks if the given string consists of one or more alphabetic characters followed by one or more digits.

import re

pattern = r'^[A-Za-z]+\d+$'
string = 'Hello123'

if re.match(pattern, string):
    print('Pattern matched!')
else:
    print('Pattern not matched.')
