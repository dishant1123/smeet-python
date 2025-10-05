# **kwargs :  use in dict ==> key  value arg 

"""def d1(**kwargs):
    for i , j in kwargs.items():
        print(f"{i}:{j}")
d1(name="smeet",age=20,city="london")

"""

# employee management system
"""
1. add employee
2. delete employee
3. update employee
4. display employee

"""

d1={}

def add_emp():
    id =int(input("enter employee id : "))
    name =input("enter employee name : ")
    salary =int(input("enter employee salary : "))
    d1[id] =[name,salary]
    print("employee added successfully")

def update_emp():
    id =int(input("enter the  emp  id you want to update : "))
    if id  in d1:
        name =input("enter the  new name : ")
        salary =int(input("enter the  new salary : "))
        d1[id]=[name,salary]
        print("employee updated successfully")
    else :
        print("employee not found")

def delete_emp():
    id =int(input("enter the  emp  id you want to delete : "))
    if id in d1:
        del d1[id]
    else :
        print("employee not found")

    
# add_emp()
# add_emp()
# print("before  update",d1)
# update_emp()
# print("after  update",d1)

# delete_emp()
# print("after  delete",d1)

"""
========EMPLOYESS MANAGEMENT SYSTEM===========

1. add employee
2. delete employee
3. update employee
4. display employee
5. exit 

"""