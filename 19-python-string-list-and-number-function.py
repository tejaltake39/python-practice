##string function
text="banana"
print(text.count("a"))

print("hello.py".endswith("py"))

print("sales_report.csv".startswith("sales"))

print("123".isdigit())
print("abs".isalpha())
print("A182".isalnum())

print("line1\nline2\nline3".splitlines())

##list functionn 
nums=[5,2,7,1]
nums.sort()
print(nums)

fruit=["Banana","Apple","Orange","Mango"]
print(sorted(fruit))

marks=[10,20,30]
print(sum(marks),max(marks),min(marks))

mylist=[1,2,3,3,1]
print(mylist.count(1))
print(mylist.index(3))

a=[1,2]
b=[3,4]
a.extend(b)
print(a)

#number function 
print(round(3.678,2))
print(abs(-50))
print(pow(3,4))
print(divmod(10,3))##why we use this command
print(sum[5,5,5],5)

##practical example
products=["mobile","laptop","tablet"]
clean=[p.strip().title()for p in products]
print(clean)

mobiles=["7666283757","9527942487","7620755539","56787"]
valid=[m for m in mobiles if m.isdigit()and len(m)==10]
print(valid)