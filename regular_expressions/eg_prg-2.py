#email id verification
import re

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
text = 'Contact us at info@example.com or support@example.org.'

matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)
