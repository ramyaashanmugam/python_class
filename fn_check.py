import time

def task1(stu_name):
    print("hai welcome",stu_name,time.ctime())
    

def task2(stu_name,age):
    return ("hello"+" " +str(stu_name)+" "+"age:"+" "+str(age)+time.ctime())


def greet(name):
    print(f"Hello, {name}! Welcome to Python programming.")

# Main function
def main():
    # Call the greet function
    user_name = input("Enter your name: ")
    greet(user_name)
    while True:
        sd=task2("vinuta",29)
        print(sd)
        time.sleep(6)
        task1("shreena")

# Check if this is the main module
if __name__ == "__main__":
    main()