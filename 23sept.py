# slicing  :  start end   step 

"""
l1=[10,20,30,40,50,60,70,900,23]
# index start  : 0    ==> l to r 
# negative index  :  -1   ==>  r to   l 
print(l1[2])
print(l1[2 :5])  # range  : 2 start  5 end index
print(l1[ : 8])
print(l1[1 : ])

print(l1[-2])
print(l1[ -2 : -6 : -1])  # no  output  
print(l1[1 : 8 :2])
print(l1[ : : 2])
print(l1[ : : -2])
print(l1[ : : -1])
"""
"""
   graph :  -7 -6  -5 -4  -3 -2 -1 0 1 2 3 4 5 6 7 8 
"""

# method  : 

l1=[10,20,30,40,50,60,70,900,23]

"""
l1.append(200)  # add in last 
print(l1)
"""
"""
l1.insert(2,"smeet")  # 2 arg  : position  ,  value 
print(l1)
"""

"""l1.pop(4)  # index number wise  remove  
print(l1)
"""
"""
l1.remove(900)  # specific  value  remove  
print(l1)
"""
"""
l2=["apple","banana","cherry","grape","kiwi"]
l1.extend(l2)
print(l1)
"""

# print(l1.count(900))

"""l2 = l1.copy()
print("l2=",l2)
"""

"""l1.sort()  # asc to desc 
print(l1)
"""
"""
l1.reverse()  
print(l1)"""

"""
l1=[23,20,30,23,50,60,70,900,23]

print(l1.index(23))  # value  ==> 
print(l1.index(23,1,10))  # 1 start index  10  endindex 
print(l1.index(23,4,10))  # 1 start index  10  endindex 
"""

# list  element  access using  loop  :

"""l1=[23,20,30,23,50,60,70,900,23]

for i in l1:  # membership operator  : 
    print(i)
"""
"""
for i in range(len(l1)):
    print(i)
"""

# task :1 
"""
ask user to enter the  element  and store in to list  and  print  the  oddsum and evensum.

input  : 5  
l1=[1,2,3,4,5]

oddsum =9
evensum =6
"""

n=int(input("enter the  number  : "))
l1=[]
for i in range(n): 
    element =int(input("enter the  element  : "))
    l1.append(element)
print(l1)
oddsum =0 
evensum =0 
for i in l1 : 
    if i % 2==0 :
        evensum +=i 
    else :
        oddsum +=i
print("oddsum  =",oddsum)
print("evensum  =",evensum)

# task :2 
"""
ask user to enter the  element  and store in to list  and  print  the  pelindrome number.
input  : 5 

l1 =[121 ,123 ,145 ,151,890]

output  : [121,151]
"""
