##17 Range+loop
#print("\n1")print1 to 5)
 
# for i in range(1,6):
#     print(i)

##even  number
# print("/n 2) even number(0-18)")
# for i in range(0,20,2):
#     print(i)

# print("/n 3)countdown from 10 to 1 ")
# for i in range(10,9,-1):
#     print(i)


# print("\n 4)loop through list using index" )
# items=["pen","Book","laptop"]
# for i in range(len(items)):
#     print(i,items)

# print("\n 5)generate employee IDs" )
# for i in range(1,100):
#     print("EMP:",i)

# print("\n 6)Yearly list")
# year=[]
# for y in range(2015,2026):
#     year.append(y)
# print(year)

# print("\n 7)clean city name using range")
# cities=["mumbai","pune","KOLkatta"]
# for i in range(len(cities)):
#     cities[i]=cities[i].strip().title()
# print(cities)


print("\n 8)extract lasst 4 digit number")
ids=["EMP-001122","EMP-001133","EMP-001144"]
for i in range(len(ids)):
    print(ids[i][-4:])

for i in range(1,4):
    for j in range(1,4):
        print(i,j)