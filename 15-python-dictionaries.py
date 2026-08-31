##14 python dictionaries 
student={"name":"rohit","age":25,"city":"mumbai"}
print(student)

##accesing values 
print(student["name"])
print(student["city"])

##adding and updating
student={"name":"rohit","age":25,"city":"mumbai"}
print(student)
student["marks"]=85
student["city"]="pune"
print(student)

#removing
student.pop("age") #pop is use for delete something 
print(student)

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))

##looping
for k in student:
    print(k,student[k])

#nested dictionary
employees={
    "E101":{"name":"rohit","age":25,"city":"mumbai"},
    "E102":{"name":"akash","age":26,"city":"pune"}
}
print(employees["E101"]["name"])

##mapping wrong to correct 
mapper={
    "mombai":"mumbai",
    "kolkata":"kolkatta"
}
print(mapper["mombai"])

