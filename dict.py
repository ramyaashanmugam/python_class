#dictionary format for single data
s= {
   "name":"ramya",
   "depart": "IT",
   "address":"india",
   "section":"b" 
}

#dictionary format for multiple data
stu_list=[
{
   "name":"ramya",
   "depart": "IT",
   "address":"india",
   "section":"b" 
},
 {
   "name":"shreena",
   "depart": "IT",
   "address":"india",
   "section":"b" 
},
{
   "name":"vino",
   "depart": "IT",
   "address":"india",
   "section":"b" 
}
]

'''print(len(stu_list))
for data in stu_list:
    print(data["name"])
    print(data["depart"])'''

import json



# function create new student dictionary data format
def c_st_data(name,dept,addr,sec):
    s={"name":name,"depart":dept,"address":addr,"section":sec}
    return s




try:
    #read json data from file
    with open("student.json", "r") as j_data:
        l_j_data=json.load(j_data)
    print(l_j_data)
    
    #try to print  only particular department students here (dept=IT)
    for i in l_j_data:
        dept=i["depart"]
        if dept == "IT":
           print(i["name"]+ " " +i["depart"])
    
    #delete particular data from file eg:name=karuna
    with open("student.json", "r") as cur_j_data:
        cur_js_data=json.load(cur_j_data)
    val=0
    found=False
    for i in cur_js_data:
        n=i["name"]
        if n == "karuna":
            found=True
            break
        val=val+1
    print(val)
    if found == True:
        #delete data from list
        del cur_js_data[val]

    print(cur_js_data)
    with open("student.json", "w") as js_data:
        js_data.write(json.dumps(cur_js_data))

    #add new student to the json file
    curr_data=c_st_data("shreena","cse","india","b")
    print(curr_data)
    with open("student.json", "w") as jas_data:
        cur_js_data.append(curr_data)
        print(cur_js_data)
        jas_data.write(json.dumps(cur_js_data))

          

except Exception as e:
    print(e)
    print()



