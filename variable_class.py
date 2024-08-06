_t="hello"
user_name="ram_shan"
print(_t,user_name)

a=b=c=100
print(a+b+c)
x,y,z="ram",22,5.8
print("name:",x,"age:",y,"height:",z)
print(f"name:{x},Age:{y},height:{z}")

print(type(x))
print(type(y))
print(type(z))

person=("ramya",30)
name,age=person
print(name)

names=["ramya","shrena","ram","ammu"]
marks=[89,90,67,56]
stu_1,stu_2,stu_3,stu_4=names
st1_m,st2_m,st3_m,st4_m=marks
print(f"student name:{stu_2} mark is {st2_m}")


x=50
print(type(x))
x="ramya"
print(x)
print(type(x)) 

#dictionary
stu_list=[{"name":"ramya","age": 23,"dept":"IT" },{"name":"shreena","age": 22,"dept":"CSE"},
          {"name":"ram","age": 25,"dept":"civil" }]
len(stu_list)
stu_1_name=stu_list[0]['name']
stu_1_age=stu_list[0]['age']
stu_1_dpt=stu_list[0]['dept']
stu_2_name=stu_list[1]['name']
stu_2_age=stu_list[1]['age']
stu_2_dpt=stu_list[1]['dept']
stu_3_name=stu_list[2]['name']
stu_3_age=stu_list[2]['age']
stu_3_dpt=stu_list[2]['dept']

print(stu_1_name,stu_1_age)
print(stu_2_name, stu_2_age)
print(stu_3_name, stu_3_age)

#please find stu1 age is  grater than 20?
print(stu_1_age >= 20)

#please list civil student from stu_list?
print(stu_1_dpt=="civil")
print(stu_2_dpt=="civil")
print(stu_3_dpt=="civil")

