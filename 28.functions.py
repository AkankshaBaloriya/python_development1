# functions= a block of reusable code
                #  place () after the function name to invike it

# positional----------------------------------------------------------------

def happy_birthday(name, age, word):
    print(f"happy birthday to {name}!")
    print(f"you are {age}old!")
    print(f"happy birthday to you {word}!")

happy_birthday("bro",10,"love")
happy_birthday("steve",14,"brother")
happy_birthday("johb",13,"friend")

# return= statement used to end a function-----------------------------------------------------------------
            #   and send a result back to  to the  caller

def add(a,b):
    z= a+b
    return z

def minus(a, b):
    z= a-b
    return z

def muntiply(a,b):
    z=a*b
    return z

print(add(2,3))
print(minus(5,3))
print(muntiply(4,3))
    

def create_name(firstname, lastname):
    firstname=firstname.capitalize()
    lastname=lastname.capitalize()
    return firstname+" "+lastname


print(create_name("akanksha","baloriya"))
print(create_name("adarsha","chouhan"))