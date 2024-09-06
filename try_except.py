import os
#print(os.getcwd())
import time

while True:
    try:
        print(os.getcwd())
        x = int(input("Please enter a number: "))
        print("your input is:",x)
        break

    except Exception as ex :
        #print("************")
        print(ex)
        time.sleep(5)
        if isinstance(ex, NameError):
            time.sleep(5)
            print("name error")
        print("please enter proper integer value")


