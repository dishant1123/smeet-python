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