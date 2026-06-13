##string indexing 
name="Tejal"
print(name[0])
print(name[1])
print(name[4])
print(name[-4])

##string slicing(veery powerful)
#syntax:string[start:end]
#example 
product="laptopmodel2024" 
print(product[0:6])
print(product[-4:])


product="laptop pro 2024"
print(product[0:6])
print(product[-4:])


text="dataanalysis"
#extracting first 4 character 
print("first 4 letters:",text[0:4]) #data

#extracting character from middle 
print(text[4:12]) #analysis

#extracting character till end 
print(text[4:])  

#extractinng characer fromg biginning
print ("from bigining:",text[:4])

#extracting character last 5 character
print("last 5 character:",text[-5:])

#skip text 
print("skip text:",text[0:12:2]) 
print("reversed:",text[4::-1])


      



