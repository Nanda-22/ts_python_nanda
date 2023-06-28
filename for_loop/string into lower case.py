str1="BALAJI"
lower_str=""

for each_character in str1:
    if (ord(each_character)>=65 and ord(each_character)<=90):
        lower_str=lower_str+chr(ord(each_character)+32)
    else:
        lower_str=lower_str+each_character
print(lower_str)
