#import function_class as fm

'''call module name fn_check.py and fc is nothing but you r creating variable for future use'''
import fn_check as fc
'''
def add(a,b):
    return a+b'''

def sum_data(*numbers):
 	return sum(numbers)


def get_name_and_age():
	user_name="kathir"
	user_age=3
	return user_name,user_age


fc.task1("ramya")
t1=fc.task2("dhana",30)
print(t1)
fc.greet("ramya")
print(fc.time.time())
#fc.time.sleep(10)
print("**********************")
#fc.main()
d1=sum_data(4,7)
print(d1)
d2=sum_data(1000,3456)
print(d2)
d3=sum_data(4,2,1,3,7,9,22,66,7,33,44,788,897,66)
print(d3)
print(get_name_and_age())
age,name=get_name_and_age()
print(name)



