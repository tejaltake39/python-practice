#Day 12-while loop 
#1 Basic While loop 
i=5
while i<=5:
    print(i)
    i+=1

#2 countdown 
n=5
while n>0:
    print(n)
    n-=1     

# 3 ask user until valid input 
num=""
while not num.isnumeric():
    num=input("Enter any number:")
print("number accepted",num)

#4 loop through list using while 
items=["apple","banana","Grapes"]
i=0
while i<len(items):
    print(items[i])
    i+=1

#5 using break
x=1
while x<=10:
    if x==5:
        break
    print(x)
    x+=1

## 6 using continue
y=0
while y<10:
    y+=1
    if y %2==0:
        continue
    print(y)
 
 ##7 password system 

password=""
attempts=0
while password!="admin123 " and attempts<3:
    password=input("Enter password:")
    attempts+=1
    if password == "admin123":
      print("login successful")
    else:
        print("Wrong Password Try Again,attemp count:",attempts)
print("attempt expired")