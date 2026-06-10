#learning data type in python 
#7 data types 

# 1 Text Data Type 
#string
customer_name="Rohit"
print("customer name is:",customer_name)
print("customerr datatype is:",type(customer_name))


# 2 Numeric Datatype 
#2.1 Interger-complete number
rating=4
order_quantity=3
print("rating:",type(rating))
print("order_quantity:",type(order_quantity))

#2.2 Float -Decimal number
order_amount=8555.76
print("ordern_amount:",type(order_amount)) 


#2.3 complex number 
a=3+4j
print(type(a))

# 3 Boolean -True/Falsse
is_paid=True
print(type(is_paid))

# 4 sequence 
# 4.1 List
cities=["Mumbaim","Pune","Delhi"] ##list can  be changeable 
print(cities)
print(type(cities))

# 4.2 Tuple
dimension=(1920,1080)## tuple can not be changeable
print(dimension)
print(type(dimension))

# 4.3 range
num=range(5)
print(list(num))
print(type(num))

# 5 Dictionary (dict)
student={
    "name" :"anvi",
    "age": 4,
    "city": "pune"
}
print(student)
print(type(student))

# 6 set
number={1,2,3,3,4}
print(number)
print(type(number))

#7 no values - noone 
remarks= None
print(remarks)
print(type(remarks))