# conditional statements : 
"""
if else : 

syntax : 

if condition : 
    print ()
else : 
    print()

"""

"""
a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))

if a>b :
    print("a is big")
else :
    print("b is big")
"""

# ladder   if  : 
"""
if con : 
    print()
elif  con : 
    print()
else :
    print()
"""

"""
a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))
c=int(input("enter the  number  : "))

if a>b and a>c :
    print("a is big")
elif b>a and b>c :
    print("b is big")
elif c>a and c>b :
    print("c is big")
else :
    print("equal")
"""

# nested if  
"""
if con : 
    if con : 
        print()
    else :
        print()
elif con : 
    if con :
        print()
    else     :
        print()
"""

"""a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))
c=int(input("enter the  number  : "))

if a>b : 
    if a>c :
        print("a is big")
    else :
        print("c is big")
elif  b>a :
    if b>c :
        print("b is big")
    else :
        print("c is big")
else :
    print("equal")
"""

# loop  : iteration  ==>  repeation  
"""
1. for  loop  :  entry control  loop
2. while  loop  :  exit control  loop
3. while True : exit  control  loop     
"""

# for loop  : 
"""
syntax : 

for (variable name) in range(start, stop , step ):
    print(variable name)

"""
# 1-100 : 

"""
for i in range(1,101):
    print(i,end=" ")
"""

# 100-1 : 
"""
for i in range(100,1,-1):
    print(i,end=" ")
"""
"""
for i in range(1,101,3):
    print(i,end=" ")
"""
# user input  : 

"""n =int(input("enter the number  : "))
for i in range(1, n+1):
    print(i,end=" ")

"""    

"""start =int(input("enter the start  : "))
end =int(input("enter the end  : "))

for x in range(start,end+1,2):
    print(x,end=" ")
"""

# prime  : 
"""
2 factors  : 1, number it self    5  factors : 1 ,5  ==>  prime  

7 factors  :1,7 prime  
12 factors  :1,2,3,4,6,12 ==>  not prime    
"""

"""
num =int(input("enter the  number  : "))   # 5 
count =0 

for i in range(1,num+1):  # 5,6  
    if num % i ==0 :  # 5 % 5   ==0 
        count +=1    # count = 2  
if count==2 :  # 
    print(num,"is a prime number")
else :
    print(num,"is not a prime number")
"""

# perfect number  : 
"""
6 factors  :1,2,3,6  == > sum  = 1+2+3 =6  ==> perfect number  
28 factors  :1,2,4,7,14,28 ==>sum 1+2+4+7+14 =28 ==> perfect 
100  factors  :1,2,4,5,10,20,25,50,100 ==>sum 1+2+4+5+10+20+25+50 ==> not perfect 

"""
