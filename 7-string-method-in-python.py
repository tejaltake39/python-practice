##string method in python
##cleaning,formating,validation,transformation
##what are strig metthod 
#1tools to clean and modify text
#2used in data cleaning &formation
#3essential for data analyst
##why string methods matters
#1clean-clean cstomers name
#2standardise-standardize city names
#3fix-fix lettter casing 
#4remove-remove unwanted spacies 
#5validate -validate emails and phone numbers 
#6-extract meaningful text 

##string methods(very important)
text1="                      hello python learners                       "
##remoce sapce 
print("remove spaces:",text1.strip())

#convert to capital letter
print("capital letters:",text1.upper().strip())#upperr for capital text ,strip for removing space#rstrip()right space remove #lstrip left space remove

#convert to proper case
print("proper case:",text1.title().strip()) #title for first element of word capital

#convert to lover case
print("lower case:",text1.lower().strip())

#remoing spacing text word  replace 
print("replace python word:",text1.replace("python","SQL").strip())

#count occurence of a leter of word
print("count of o",text1.count("o"))

#chech if text start with something
print("start with hello:",text1.strip().startswith("hello"))

#chech if only numbers are present in data 
mobile="736643655"
print("is numeric:",mobile.isnumeric())

msg="welcome to python course"

#split string in list of word
words=msg.split()
print("word list:",words)

#join with hyphon
joined_text="_".join(words)
print(joined_text)

#find position of letter
print("index of p:",msg.find("p"))

#extract domain
email="student@example.com"
domain=email[email.find("@")+1:]
print(domain)