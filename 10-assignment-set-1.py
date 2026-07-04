#assignment 1 multi level varification sysytem 
#try by me  Q=1
secuity_code=int(input("enter your security code"))
if secuity_code==5566:
 department=(input("enter your department:"))
  if department.lower()=="finance":
  access_level=input("enter your access level:")
    if access_level>=5:
    print("access level granted :welcome to the meeeting")
    else:
    print("insufficient access level")
  else:
  print("access denied:department is not allowed")
else:
 print("invalid security code")

 ##
 #code is correct syntax error is here

#solution Q2
reg=int(input("enter your reg no"))
if reg==1221:
 subject=input("enter your subject")
  if subject.lower()==python:
    password=int(input("enter your password"))
    if password==8888:
    else:
     print("wrong password")
  else:
 print("subject is not available")
else:
print("registration failed")
