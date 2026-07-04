##day 11 for loop 
##1 bsic loop 
for i in range(1,10):
    print(i)

##2 print character 
word="python"
for alphabet in word:
    print(alphabet)

word2="sql"
for j in range(1,11):
    print(word2)

## loop through list 
items=["pen","book","laptop"]
for item in items:
    print(item)

##4 even number 
for n in range (0,21,2):
    print(n)

#for odd number
for n in range (1,21,2):
    print(n)

##total calculation 

marks=[78,82,90]
total=0
for m in marks:
    total+=m
print("total:",total)


#6 clean city names 
cities=["mumbai","delhi","kolkatta","pune"]
cleaned=[]
for c in cities:
    cleaned.append(c.strip().title())
print(cleaned)


#7loop with if conditionn 
nums=[5,12,3,18,7]
for n in nums:
    if n>10:
        print(n,"in grater than 10")
    else:
        print(n ,"in not greater then 10")

