#program for append+ function
try:
    f=open("test2.txt","a+")
    data="This file write mode"
    print(f.write(data))
    f.close()
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

finally:
    print("File operations completed")
