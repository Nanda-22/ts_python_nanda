student_details={"Rno":100,"Name":"Sai","location":"Hyderabad"}
print(student_details.keys())
print(student_details.values())
print(student_details.items())

for each_key in student_details.keys():
    print("Key is",each_key ," and value is",student_details[each_key])

for (each_key,each_value) in student_details.items():
    print("Key is",each_key ," and value is",each_value)
