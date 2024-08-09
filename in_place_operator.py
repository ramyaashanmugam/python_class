import operator
a=55.90
b=4
print("Original, a =", a) 
'''
# In-place Addition  
a += b  
a=a+b #dynamic typing
'''
# The above operation is equivalent to  
#a = a + b  
b+=a
#a = operator.iadd(a, b)  
a = operator.__iadd__(a, b)  
print("Updated, a =", a)  
print("Updated, b =", b) 
