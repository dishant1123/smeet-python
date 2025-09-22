# match  : 
"""
1. addition  2 . sub  3 . mul 

match  choice :
    case 1 : 
"""
"""while True :
    a=int(input("enter the  number 1 :"))
    b=int(input("enter the  number 2: "))
    while True :
        print("1.addition")
        print("2.sub")
        print("3.mul")
        print("4.div")
        print("5.enter the  new  number  : ")
        print("6.exit")
        choice =int(input("enter the  choice  : "))

        match choice :
            case 1 :
                print(a+b)
            case 2 :
                print(a-b)
            case 3 :
                print(a*b)
            case 4 :
                print(a/b)
            case 5 :
                break 
    sure =input("are you sure  : ")
    if sure =="yes" :
        break
    else :
        continue
"""

# nested loop  : 


# 2  range  : ==> amg print 

"""
153 :  3 digit   :

1**3   5 **3  3**3 
1      125    27 

sum = 1+125 +27 =153  

1634 :  4 digit 

1**4  6**4 3 **4 4**4 
1    1296  81     256 
sum =1634  amg 

s1=12341234567   # data type :  int   ==>  convert  string  ==> "1234"
print(len (str(s1)))
""" 

"""start  =int(input("enter the starting value  : "))
end  =int(input("enter the starting value  : "))

for i in range(start, end +1):   # 154  10000 
    sum =0
    digit =  len(str(i))  # 3 
    temp =i   # temp =153 
    for j in range(digit):  # 2,3 
        r = temp % 10       # r = 1 % 10 = 1   
        sum = sum + pow(r,digit)  # sum = 153  
        temp  = temp //10         # temp  =0  
    
    if sum ==i: 
        print(i,end=" ")

"""
# perfect in range  :  start  end   1 -10000 ==> 