#if else conditon 
#why we use =for disicion making in python 
#what is if else ?1=python in decision making tool 2 executes code based on conditions
#why it matters=1 filter data 2 validate inputs 3 categorize values 

##if else condition 
age=int(input("enter your age:"))

if age>=18:
    print("qualified for voting")
else:
    print("not qualified")

##discount checker 
amount=int(input("enter your amount"))
if amount>=1500:
    print("eligible for discount")
else:
    print("not eligible for discount")

##if elif -else condition 
mark=int(input("enter your marks"))
if mark>=90:
    print("Grade A")
elif mark>=70:
    print("Grade B")
elif mark>=35:
    print("Grade c")
else:
    print("fail")

#sales code
sales=65000
if sales>=100000:
    print("high performance")
elif sales>=500000:
    print("average performance")
else:
    print("low performance")

#city code 
city="Delhi"
if city.lower()=="delhi":
    print("city matched")
else:
    print("city noy matched")


##password programme
password=input("enter your password")
if password.lower()=="admin@1":
    print("login successful")
else:
    print("wrong password")

#email validation 
email=input("enter your email")
if "@" in email and "."in email:
    print("valid email")
else:
    print("invalid email")

#advance missing data check  

value="adf"

if value=="":
    print("missing data found")
else:
    print("data available ")