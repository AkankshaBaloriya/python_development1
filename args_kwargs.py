# function---------------------------------
# args   = allow you to pass multiple non-key arguments,and we can give multiple parameters with only one args,
# args creat a tuple
# **kwargs =allows you to pass multiple keyword-arguments ,kwargs creates a dictionary
#                     *unpacking operator
#                     1. positional  2. default  3.keyword  4.arbitrary


# arbitrary--------------------------------------------------------------------------

def add(*args):     # here arg means its a tuple in which we can store so many collection
    total=0         # instead of "*args" we can write "*any_name" as well
    for arg in args:
        total+=arg
    return total

print(add(1,2,3,4,5))

def name(*args):
    print(f"akanksha is {args[0]}")
    print(f"aadarsh {args[1]}")
    
print(name("akki","aash"))

def names(*name):
    for arg in name :
        print(arg,end=" / ")
    print()

names("harry","charlie","ariana","delton")

# **kwargs-----------------------------------------------------------------------------------------------
# same as args but in args we can not set keyword but in kwargs we can
# kwargs create dictionary ,args create tuple
def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

address(first="indore",second="M.P",third="india",fourth="asia")
print()
address(first="name",second="address",third="class",fourth="place")

def lable(*args, **kwargs):#args followed by kwargs
    for arg in args:
        print(arg)
    print()
    for key, value in kwargs.items():
        print(f"{key}  {value}")

lable("dr","zeus","is","villain",
name="akanksha",last_name="baloriya")

