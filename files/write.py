#program for write function
try:
    f=open("test1.txt","w")
    data="This file write mode"
    print(f.write(data))
    f.close()
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

finally:
    print("File operations completed")
