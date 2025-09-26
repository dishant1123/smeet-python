"""
1. Ask user to give name and marks of 10 different students. Store them in dictionary.

3 name  marks  : 
ram  90  sita   78  ravan  92 
d1= {"ram":90,"sita":78,"ravan":92}

2. Sort the above dictionary in ascending order of Marks.
d1={"sita":78,"ram":90,"ravan":92}

"""
"""d1={}
for i in range(3):
    name =input("Enter name of student:")
    marks=int(input("Enter marks of student:"))
    d1[name]=marks
print(d1)#{'ram': 90, 'sita': 78, 'ravan': 99}

sorted_value =sorted(d1.values())
print(sorted_value) #[78, 90, 99] 
d2={}
for j in sorted_value: #[78, 90, 99]
    for name ,marks in d1.items(): #{'ram': 90, 'sita': 78, 'ravan': 99}
        if j ==marks:
            d2[name] =j 
print(d2)

"""

"""
3. Make a Python program to count letters of the word: MISSISSIPPI. 
Your program should store them in a dictionary as: {"M":1, "I":4, "S":4, "P":2}. Next, generalize this program for any word entered by user.

"""

"""n=input("Enter the word:") #MISSISSIPPI
d={}
for i in n :  # m 
    if i not in d :  # 
        d[i]=1    # d[m]=1 d[i]=1  d[s]=1 
    else :
        d[i]+=1   # d[s] =2 
print(d)
"""

l1=[1,2,3,3,4,4,5,5,6,6,7,7,8,9]
# output [1,2,3,4,5,6,7,8,9]
