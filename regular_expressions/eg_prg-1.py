#example program for hiding the date from givem string
import re

pattern = r'\b\d{2}-\d{2}-\d{4}\b'
string = 'John\'s birthday is on 12-31-1990. Lisa\'s birthday is on 06-15-1985.'
new_string = re.sub(pattern, "XX-XX-XXXX", string)
print(new_string)
