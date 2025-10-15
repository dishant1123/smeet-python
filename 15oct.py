# local  variable : with  function accessible  only   

"""def local_var():
    a=10 
    print(a)
local_var()
"""
# print(a)  # local variable not  accessible  outside the function 

# global variable  :  with func ,  outside func  also accessible

"""a=100
def global_var():
    print(a)

global_var()
print(a)  # accessible outside the function
"""

# modify the  global variable  using  global keyword . 
"""a=10 
def global_var():
    global a 
    a=100 
    print(a)
global_var()
print(a)
"""

# random  module  : 

import random as r 

# print(r.random())  # float  value  between 0 and 1  ==> 1 excluded 
# print(r.randrange(1,10,2))  # 10  excluded 
# print(r.randint(1,10))  # both value included 
# print(r.choice([1,2,3,4,"smeet","U.K"]))
# print(r.choices([1,2,3,4,"smeet","U.K"],k=3))

"""
l1=[1,2,3,4,"smeet","U.K"]
print(l1)
r.shuffle(l1)
print(l1)

"""
# game  : 
"""
1.rock 
2.paper 
3.scissor 

user vs computer 

===> function  ==> choice  ["rock","paper","scissor"]
                   randint (1,3)  # both  value  included  
                   
10 time  :  for loop  ,  while   

user_score = 0 com_score = 0 

if u==1 and c==1 or u==2 and c==2 or u==3 and c==3 :
    print ("tie)   ==> user 0  comp  0 

elif u==1 and c==3  or u==2 and  c==1   or u==3 and  c==2    
    print("user wins )   ==> userscore +=1 
else :
    print("com win") ==> comp_score +=1
    
display  :  user_score com_score   ==> win decided  
"""

