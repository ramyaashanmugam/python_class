print('hello')
fname='ramya'
print(fname)
lname="shanmugam"
print(lname)
triple_quoted = '''This is a multi-line string in Python.'''
print(triple_quoted)
another_triple_quoted = """This is another multi-line string."""
print(another_triple_quoted)
v3='"shanmugam"'
print(v3)

username=fname+" "+lname
print("username =",username)
print(username* 3)
len_uname=len(username)
print(username[len_uname-13])
print(username[2])

#slicing
print(username[:5])

#uppercase
print(username.upper())

#lowercase
print(username.lower())

#title
print(username.title())

#replace
print(username.replace())