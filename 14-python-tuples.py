##14 tuple in python 
#create tuple
fruits=("apple","Banana","mango")
print(fruits)

#indexing
print(fruits[0])
print(fruits[1])

#slicing
nums=(10,20,30,40)
print(nums[1:3])

#looping
colors=("red","blue","green")
for c in colors:
    print(c)

color=("red","bluE","GREEn")
clean=[]
for i in color:
    clean.append(i.strip().title())
print(clean)

#tuple length
color=("red","bluE","GREEn")
print(len(color))
 
#concatenation
a=(1,2)
b=(3,4)
print(a+b)


##packing and unpacking 
data=("laptop",4500,"Black")
product,price,color=data
print(product,price,color)

##nested tuple inside list 
employees=[("E101",'Rohit',"pune"),("E102","sneha","Mumbai")] 
for eid,name,city in employees:
    print(eid,name,city)

