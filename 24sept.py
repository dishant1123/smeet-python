"""l1 =[121 ,123 ,145 ,151,890]
l3=[]

for i in l1 :
    if str(i) ==str(i)[: : -1]:
        l3.append(i)
print(l3)
"""

# tuple  : immutable sequence of elements

"""t1 =(1,3,4,5,6,7,8,8j,98.45)
print(t1)
print(type(t1))

t2= 1,2,3,4,5,6,78.90,8j
print(t2)
print(type(t2))
"""

# built in function  :  len min max  sorted sum 

t1=(1,2,3,4,5,90,100,23)

"""print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))
print(sum(t1))
"""

# update : 

"""t1[2] ="smeet"
print(t1)  # error : tuple is immutable
"""

#slicing  : 
"""
t1=(1,2,3,4,5,90,100,23)

print(t1[2])
print(t1[-2])
print(t1[2 :5])
print(t1[2 : 6 :2])
print(t1[ :  :-2])
print(t1[ :  :-1])

print(sorted(t1))  # asc to desc 
print(sorted(t1,reverse=True))  # desc to asc
"""

# method  : 

"""t1=(100,2,3,4,5,90,100,23)

print(t1.count(100))
print(t1.index(100))
print(t1.index(100,1,20))
"""

# task :1 
"""
input  : t1=  (1,2,3,4,5,6,7,8,9,10)
output : t1 =(1,2,3,4,5,6,7,8,9,10,"smeet")
"""