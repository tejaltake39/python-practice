#input and type casting 
name=input("Enter your name :")
print("welcome",name)

#typecasting
age=int(input("enter  your age:"))
print(type(age))
age=age+5
print("your age is:",age)

temp=30.5
temp=int(temp)
print(type(temp))

temperature=float(input("enter todays temp:"))
print(type(temperature))


#convert number to string 
sales=50000
text="total sales:"+str(sales)
print(text)

#total sales calculator
product=input("product name:")
quantity=int(input("enter quantity sold:"))
prize_per_unit=float(input("enter prize per unit:"))
total_sales=quantity*prize_per_unit
print("product:",product)
print("total saless unit:",total_sales)

#practice calculation 
fnum=int(input("Enter fist number:"))
snum=int(input("Enter second number:"))
sum=fnum+snum
print(sum)

#Assignment question

name=input("Enter Your Name:")
Basic_salary=float(input("Enter your Basic salary:"))
Bonus=float(input("Enter Bonus Amount:"))
tax_percentage=float(input("Enter tax %:"))


gross_salary=Basic_salary+Bonus
tax_amount=gross_salary*(tax_percentage/100)
net_salary=gross_salary-tax_amount

