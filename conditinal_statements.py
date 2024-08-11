'''# if statement
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
'''
''' if,elif,else prerequest
1. take input from user stutent name
2. need to check with student name == ramya or shreena
3. if student name satisfy print( student gelongs to IT depatment)
4. else print student doesnot belongs to IT
'''
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

'''
create 5 student name list1 with ramya,shreena,mamo,vino,ram
create 5 student name list2 with raju,prasanna,radha,krish,adidev
get input from user student name
student present in list1 print student belongs to class A or ckck with list2 print student belongs to class b
otherwise print student does not belongs to A or B section need to ckeck with different section

'''
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
'''
'''
units = float(input("Enter the total units of electricity consumed: "))

# Initialize the bill amount
bill_amount = 0

# Calculate the bill based on the given criteria
if units > 300:
    bill_amount += (units - 300) * 5
    units = 300
if units > 100:
    bill_amount += (units - 100) * 2

# Display the calculated bill amount
print(f"The total electric bill is: {bill_amount:.2f} Rs")
'''

numbers = [10, 40, 3, 40]
threshold = 5

if numbers[0] >= threshold:
    if numbers[1] >= threshold:
        if numbers[2] >= threshold:
            if numbers[3] >= threshold:
                print("all elements in a list are greater than threshold value")
            else:
                print("all elements in a list is not greater than threshold value")
        else:
            print("all elements in a list is not greater than threshold value")
    else:
         print("all elements in a list is not greater than threshold value")
else:
    print("all elements in a list is not greater than threshold value")

#if any of the element in a lis is even or not
l1=[5,9,8,9]
if l1[0] %2 !=0:
    if l1[1] %2 !=0:
     if l1[2] %2 !=0:
      if l1[3] %2 !=0:
       print("all elenment in a list is odd")
      else:
         print("even")
     else:
         print("even")
    else:
        print("even")
else:
    print("even")

val=5
out=''
for i in range(val):
   out= out+str(i+1)
print(out)


l3=[2]
print(len(l3))
'''if l3 != []:
   print("list is not empty")
else:
   print("list is empty")
'''
if len(l3) == 0:
   print("list is  empty")
else:
   print("list is not empty")

if not l3:
   print("list is  empty")
else:
   print("list is not empty")
   
INTEGER =10.0
FLOAT =10
if type(INTEGER) == float:
    INTEGER=int(INTEGER)
if type(FLOAT) == int:
    FLOAT=float(FLOAT)
print(INTEGER)
print(FLOAT)    
      
units = float(input("Enter the total units of electricity consumed: "))
# Initialize the bill amount
bill_amount = 0
# Calculate the bill based on the given criteria
if units > 300:
    bill_amount += (units - 300) * 5
    units = 300
if units > 100:
    bill_amount += (units - 100) * 2
# Display the calculated bill amount
print(f"The total electric bill is: {bill_amount:.2f} Rs")


