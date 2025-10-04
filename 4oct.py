# method : 

# index rindex find rfind  

s1="my name is smeet gajjar."

"""print(s1.index("a"))
print(s1.index("a",5,20))
print(s1.index("a",19,22))
print(s1.index("name"))
print(s1.index("ame"))

print(s1.find("a"))
print(s1.find("name"))
"""
"""print(s1.rindex("a"))
print(s1.rindex("e"))

print(s1.rfind("a"))
print(s1.rfind("e"))
"""
# split rsplit partition  rpartition : 

s1="my name is smeet gajjar."

"""print(s1.split())
print(s1.split("a"))
print(s1.split("name"))

# hw :  split  - rsplit  diff : 
print(s1.rsplit("a"))


print(s1.partition("a"))  # 3 part divide
print(s1.partition("name"))  # 3 part divide

print(s1.rpartition("a"))
print(s1.rpartition("e"))
"""

# replace :

"""s1="my name is the the  smeet gajjar."

print(s1.replace("name",""))
print(s1.replace("the",""))
print(s1.replace("the","",1))
"""

"""
3.Write a Python code that prints the index numbers of all the occurrences of "o" in a given string . 

	input string : "i am going to goa next month."
	output  :     first "o" index number is  : 6 
		      2nd  "o"  index number is : 12
		      3rd  "o"  index number is  :15 
		      4 th "o"  index number is  :18
		      5 th "o"  index number is  :27

"""

"""
4.Write a Python code that asks a string from user and replace the first occurance of " " with "_" and last occurance of " " with "#".'''
input string: Keep yourself mute while not speaking.
output: Keep_yourself mute while not#speaking.
hint  :  replace + slicing  
"""

"""6.Write a program to make a new string with the word "the" deleted in the given string.
input string: This is the lion in the cage.
output: This is lion in cage.

7.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""


# function  : 
"""
1. no arg no return 
2. with arg no return 
3. no arg  with return 
4. with arg  with return

"""
# no arg  no return  
"""def func1():  # def key word func1 function anme  
    a=10 
    b=90   # function  intialization 
    c=a+b 
    print(c)
func1()  # function  call 
"""
# with arg  no return
"""def func1(a,b):
    c=a+b
    print(c)

a=int(input("enter a number"))
b=int(input("enter b number"))
func1(a,b)
"""

# no arg  with return
"""
def func1():
    a=int(input("enter a number"))
    b=int(input("enter b number"))
    c=a+b
    return c 

print(func1())
"""

# with arg  with return

"""
def func1(a,b):
    c=a+b
    return c 
a=int(input("enter a number"))
b=int(input("enter b number"))
    
print(func1(a,b))
"""
# *args : only taken number of argument 
"""def func1(*args):
    
    return sum(args)  # sum  ==> built in function   

print(func1(1,34,24,456,778,345,5667,2233))
"""

def d1(*args):
    sum =0 
    for i in args:
        sum = sum +i 
    print(sum)
d1(1,2,3,4,5,6,7,8,9,10)

# next session  :  **kargs , app ==> menu driven  ==> python 