# dat 16 sets 
#creat sets
fruits={"Apple","Banana","Apple","mango"}
print(fruits) #it does not repeat the values 

#add item
fruits.add("Grapes")
print(fruits)

#remove item
fruits.discard("Banana")
print(fruits)

#set operation 
a={1,2,3}
b={3,4,5}
print("union:",a|b)
print("intersection:",a & b)
print("difference:",a - b)
print("symmmetric difference:",a ^ b)

#remove duplication 
cities=["mumbai","pune","Delhi","mumbai"]
unique=set(cities)
print("unique cities:",unique)

#missing values 
list1={"SQL","Excel","Power bi"}
list2={"SQL","Power bi"}
missing=list1-list2
print("missing:",missing)

##common skill
DepA={"SQL","Excel","python"}
DepB={"Excel","python","powerbi"}
print("common skill:",DepA & DepB)