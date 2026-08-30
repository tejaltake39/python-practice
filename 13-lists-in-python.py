# day 13 lists in python 
fruits=["Apple","Banana","Mango"]
print(fruits)
 
##indexing 
print(fruits[0])
print(fruits[-1])

## update list 
fruits[1]="orange"
print(fruits)

##add item 
fruits.append("Grapes")

##position change
fruits.insert(1,"papaya")
print(fruits)

# remove item 
fruits=["Apple","Banana","Mango"]
print(fruits)
fruits.remove("Mango")
# fruits.pop() ##optional
print(fruits)

#slicing 
nums=[10,20,30,40,50]
print(nums[:3])
print(nums[-3:])

##looping 
fruits=["Apple","Banana","Mango"]
for f in fruits:
    print("fruits:",f)

##clean city name 
raw=["mumbai","DELhi","PUne"]
clean=[]
for c in raw:
    clean.append(c.strip().title())
print(clean)

##Replace wrong spelling 
wrong=["kolkatta","bengluruu"]
fixed=[]
for i in wrong:
    i=i.replace("kolkatta","Kolkata").replace("bengluruu","Bengluru")
    fixed.append(i)
print(fixed)