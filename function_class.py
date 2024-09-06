import time

def task1(stu_name):
    print("hai welcome",stu_name,time.ctime())
    
def task2(stu_name,age):
    return ("hello"+" " +str(stu_name)+" "+"age:"+" "+str(age)+time.ctime())

while True:
    sd=task2("ramya",29)
    print(sd)
    time.sleep(6)
    task1("shreena")
