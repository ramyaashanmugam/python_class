#for loop
#n1=input("enter name 1:")
'''l1=[]
for i in range(5):
    #print(i)
    name=input("enter"+ " "+ str(i+1)+" "+"name:")
    l1.append(name)

print(l1)
'''
#Write a Python program to print numbers from 1 to 10 using a for loop.
'''
for i in range(10):
    print(i+1)'''
    
#Write a Python program to calculate the sum of the first 20 natural numbers using a for loop.
'''sum_nat=0
for i in range(6):
    print("initially",sum_nat)
    print("my current i value:",i)
    sum_nat=sum_nat+i
    print("after adding my i value",sum_nat)
print("my final output is",sum_nat)'''

#Given a list fruits = ['apple', 'banana', 'cherry', 'date'], write a Python program to print each fruit in the list using a for loop.
'''
fruits = ['apple', 'banana', 'cherry', 'date']
for name in fruits:
    print(name) '''

#Write a Python program to print the multiplication table of 5 using a for loop.
'''
for i in range(1,6):
    print(str(i) + "*" + "5 =",i*5)'''

#Write a Python program that takes a list of numbers and prints only the even numbers using a for loop.
'''
list_1=[4,5,7,8,9,10,33,22,55,66]
list_2=[]
list_3=[]
for num in list_1:
    if num %2 ==0:
        list_2.append(num)
    else:
        list_3.append(num)
print(list_1)
print("even:",list_2)
print("odd:",list_3)
'''

#Write a Python program to calculate the sum of all elements in a list numbers = [3, 5, 7, 9, 11] using a for loop.
'''numbers = [3, 5, 7, 9, 11]
b=0
for ramya in numbers:
    b=b+ramya
print(b)'''

#Write a Python program to count the number of times the character 'a' appears in the string "banana" using a for loop.
'''string_d="banana"
val_a=0
for r in string_d:
    print(r)
    if r == 'a':
        val_a=val_a+1
print(val_a)
'''

#Write a Python program to reverse a given string using a for loop. Example: Input: "Python", Output: "nohtyP".
d="python"
word=""
for r in d[::-1]:
    word=word+r
print(word)

'''
for num in range(1, 51):  # Range from 1 to 51 (inclusive)
    if num > 1:  # 1 is not a prime number
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, "is a prime number")'''

for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()

for j in range(0,3+1):
    print("D",end=" ")