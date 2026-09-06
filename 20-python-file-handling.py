#day 20 file handling 
##1)reading full file
with open("sample.txt","r")as f:
    print(f.read())

##2 ewading line by line
with open("sample.txt","r")as f:
    for i in f:
        print(i.strip().title())

##3 writing (overwrite)
with open("notes.txt","w")as f:
    f.write("day 20-file Handling\n")
    f.write("learning read and write.\n")

##4 appending 
with open("notes.txt","a")as f: ##using a for adding line 
    f.write("appendinng new content.\n")

##5 cleaning data in file 
cleaned=[]
with open("sample.txt","r")as f:
    for line in f:
        cleaned.append(line.strip().title())
with open("cleaned_uotput.txt","w") as f:
    for city in cleaned:
        f.write(city+"\n")

##6 counting lines
count=0
with open("sample.txt","r")as f:
    for _ in f: ## - for each line 
     count+=1
print("total lines:",count)