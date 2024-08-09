# if statement
x=5
if x == 5:
    print(x)

# else if statement
a=11
if a== 10:
    print(a)
else:
    print("not a 10 is different value",a)

#given val even num or not
val=int(input("enter number:"))
if val %2==0:
    print("gevin value is a even number")
else:
    print("given value is odd number") 

''' if,elif,else prerequest
1. take input from user stutent name
2. need to check with student name == ramya or shreena
3. if student name satisfy print( student gelongs to IT depatment)
4. else print student doesnot belongs to IT
'''

student=input("enter student name:")
if student=='ramya':
    print("student belongs to IT depatment")
elif student=='shreena':
    print("student belongs to IT depatment")
else:
    print("student does not belongs to IT depatment")


student=input("enter student name:")
#if student=='ramya'.upper() or student=='ramya'.lower() or student=='ramya'.title() or student.lower()=='ramya':
 #   print("student belongs to IT depatment")
#elif student=='shreena'.upper() or student=='shreena'.lower() or student=='shreena'.title() or student.lower()=='ramya':
 #   print("student belongs to IT depatment")
if student.upper()=='ramya':
    print("student belongs to IT depatment")
elif student.lower()=='shreena':
    print("student belongs to IT depatment")
else:
    print("student does not belongs to IT depatment")


'''
create 5 student name list1 with ramya,shreena,mamo,vino,ram
create 5 student name list2 with raju,prasanna,radha,krish,adidev
get input from user student name
student present in list1 print student belongs to class A or ckck with list2 print student belongs to class b
otherwise print student does not belongs to A or B section need to ckeck with different section

'''

list1=["ramya","shreena","mano","vino","ram"]
list2=["raju","prasanna","radha","krish",'adidev']
student_name=input("enter the student name with lowercase:")
if student_name in list1:
    print("student belongs to class A")
elif student_name in list2:
    print("student belongs to class B")
else:
    print("student does not belongs to A or B section need to ckeck with different section")

