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

# mcq : 
"""
t1 = (1,2,3,4,[6,7,8] ,90)
t1[4].append("smeet")
print(t1)

a.1,2,3,4,[6,7,8,"smeet"] ,90
b.1,2,3,4,[6,7,8],"smeet",90
c.1,2,3,4,"smeet",[6,7,8],90
d. error beacuse tuple is immutable.
"""

"""t1 = (1,2,3,4,[6,7,8],90)
#     0 1 2 3 4
t1[4].append("smeet")
print(t1)
"""

# dict : mutable  sequence of key-value pairs.

"""
d1={"phy":90,"che":78} 
# phy ==> key value  90   che ==> key 78 

print(d1)
print(type(d1))

d2={34 :78 ,99 :"maths"}
print(d2)
"""

# update  or add : 

"""
d1={"phy":90,"che":78} 

d1["maths"]=93  # add 
d1["phy"]=89  # update 
print(d1)
"""

# built  in function :  len  min  max  sorted  sum

"""
d1={"phy":90,"che":78} 

print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))
"""

# no slicing  in dict : 

"""
d1={"phy":90,"che":78} 
print(d1[0])  # error : bcz of  no slicing  poss in dict.
"""

# method : 
d1={"phy":90,"che":78} 

"""d1.clear()
print(d1)
"""

"""d2=d1.copy()
print(d2)
"""

"""print(d1.keys())
print(d1.values())
print(d1.items())
"""
d1={"phy":90,"che":78,"maths":99} 

# print(d1.get("phy")) # arg : key 

"""l1= ["dishant","smeet"]
# {"dishant":100,"smeet":100}

d2 =dict.fromkeys(l1,100)
d2["dishant"]=101
print(d2)

d1.update(d2)
print(d1)
"""
"""d1.pop("phy")
print(d1)
"""
"""d1.popitem()
print(d1)
"""
"""d1.setdefault("ss",100)
print(d1)
"""

# list  , tuple  ,dict:   
"""
3 name  marks  : 

ram  90  sita   78  ravan  92 

d1={"ram":90,"sita":78,"ravan":92}
"""
