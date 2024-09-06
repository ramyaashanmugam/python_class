#create a list
'''
try:
    var1=[1,5,7,8,10]
    print(var1[3])
    x = int(input("Please enter a number: "))
    print("your input is:",x)
except Exception as e:
    #print(e)
    if isinstance (e,IndexError):
        print("index error so please provide proper index val")
    if isinstance(e,ValueError):
        print("please enter proper integer value")

'''        
#creating string list
fruits = ["apple", "banana", "cherry"]

# A list of mixed data types
mixed_list = [1, "hello", 3.14, True]

# A list containing another list
nested_list = [1, 2, [3, 4], 5]

print(nested_list[2][1])
print(nested_list[2])

veg=["carrot","tomatto"]
#fruits.append(veg)
print(fruits)

fruits.extend(veg)
print(fruits)

l1=[5,8,9,6,4,0,3,1,2]
#l1.sort()
#print(l1)
l1.reverse()
print(l1)
