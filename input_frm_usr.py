
input_user=input("enter your name:")
print("hello",input_user)
age=input("enter your age:")
print(input_user,"age is",age)
print(input_user+" "+"age is"+" "+age)
print(f"Hello, {input("enter your name:")}!\n your age is {age}.")

a=int(input("enter a value="))
b=int(input("enter b value="))
print("after adition a+b=",a+b)

a=input("enter a value=")
b=input("enter b value=")
print("after adition a+b=",a+b)


#multiple inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Name: {name}, Age: {age}")


data = input("Enter your name and age , mark separated by a space: ")
name, age ,mark = data.split()
print(data)
#age = int(age)
print(f"Name: {name}, Age: {age},mark:{mark}")



from getpass4 import getpass

user_name = input("Enter your username: ")
password = getpass('Password: ')

print(user_name,password)


name=input("enter name?")
age=input("enter age?")
print("name:",name,",","age:",age)

