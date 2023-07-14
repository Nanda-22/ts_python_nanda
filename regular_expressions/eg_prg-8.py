#program for phone number validation
import re

pattern = r'^\d{3}-\d{3}-\d{4}$'
phone_number = '123-456-7890'

if re.match(pattern, phone_number):
    print('Phone number is valid.')
else:
    print('Phone number is not valid.')
