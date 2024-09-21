
l1=["ramya","shreena"]


#to create a own/cutom error
class listError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class AgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

while True:
    try:
        val= int(input("enter value:"))
        print(os.getcwd())
        name=str(input("enter name to search in list:"))
        if name not in l1:
            raise listError("name not found in list")
        else:
            print(name,"present in list")

        age=int(input("enter your age to check voting eligibility:"))
        if age < 16:
            raise AgeError("not eligible for voting")
        else:
            print("you are eligible for voting")

    except Exception as e:
        print(e)
        if "name 'os' is not defined" in str(e):
            import os
            print("os imported")
        if "invalid literal for int() with base 10" in str(e):
            print("please enter integer value")
        if "name not found in list" in str(e):
            print("please enter any name ",l1)
        if "not eligible for voting" in str(e):
            print("you are not eligible for voting")



