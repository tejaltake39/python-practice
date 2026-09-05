##day 18 function(def,return)

def greet():
    print("Hello python learners")

greet()

def welcome(name):
    print("welcome",name)
print("Tejal")

def add(a,b):
    print("A+B:",a+b)
add(10,30)


def add(a,b):
    return a + b 

sum=add(10,40)
print(sum)

def multiple(x):
    return x*2

result=multiple(add(30,10))
print(result)

##
def clean_text(value):
    return value.strip().title()

output=clean_text("   MumBai ")
print(output)

##
def fix_city(city):
    city=city.lower().strip()
    city=city.replace("MOMbai","Mumbai")
    city=city.replace("KOLKATaa","Kolkatta")
    return city.title()
print(fix_city("    Mombai      "))



def clean_list(values):
    cleaned=[]
    for v in values:
        cleaned.append(v.strip().title())
    return cleaned
print(clean_list(["delhi","mumbai","pUne"]))









