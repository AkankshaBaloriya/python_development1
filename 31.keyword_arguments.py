# keyword arguments =an argument preceded by an identifier
#                   helps with readability
#                   order of arguments doesn't matter
#                   1. positiotional  2. default  3. keyword   4. arbitrary

# keyword---------------------------------------------------------------------------------------

def hello(greeting, title,first,last):
    print(f"{greeting} {title}{first} {last}")

hello(last="baloriya",greeting="hello",title="mr.",first="adarsha")  #doing this is calles keyword argument in 
#  positional argument we have to write value in right sequence but if we give it keyword than value can be written
# randoml sequence

for x in range(1,11):
    print(x,end=" ")

print("1","2","3","4","5",sep="_")

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone=get_phone(country=1,area=123,first=456,last=789)
print(phone)