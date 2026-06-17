#nested if and multiple condition
#nested if means putting if innside another if 
print("check your eligibility")
age=int(input("enter your age:"))
if age>=18:
    id_no=int(input("enetr your id number:"))
    if id_no==1722:
        print("you can enter")
    else:
        print("wrong id no")
else:
    print("you are underage")

#multiple conditions (and) 
age=int(input("enter your age"))
residence=input("are you indian?")

if age>=18 and residence.lower()=="yes":
    print("your eligible to drive")
else:
    print("your not eligible to drive")
