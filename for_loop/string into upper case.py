str1="Balaji"
upper_str=""

for each_character in str1:
    if (ord(each_character)>=97 and ord(each_character)<=122):
        upper_str=upper_str+chr(ord(each_character)-32)
    else:
        upper_str=upper_str+each_character
print(upper_str)

