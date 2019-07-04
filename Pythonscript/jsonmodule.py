import json

employee_data='''

{
"people":[
{
"name":"Mahesh",
"email":"mahesh.patlo@gmail.com",
"married":"true"
},

{
"name":"Ramesh",
"email":"ramesha.totalo@gmail.com",
"married":"false"
}
]}

'''

print(employee_data)

data=json.loads(employee_data)

print(data)