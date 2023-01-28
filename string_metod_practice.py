a=input("enter the username")

b=len(a)
# print(b)
c=a.isalpha()
# print(c)
d=a.find(" ")
# print(d)

# if b>12:
#     print("contains more than 12 character")
# elif d>=0:
#     print("no space allowd")
# elif c is False:
#     print("only alphabet allowd")
# else:
#     print(a) 

# BOTH WORKS CORRECT BUT THE ABOVE ONEIS CODED BY ME AND BELOW ONE BY BRO CODE

if len(a)>12:
    print("contains more than 12 character")
elif not a.find(" ")==-1:
    print("no space allowd")
elif not a.isalpha():
    print("only alphabet allowd")
else:
    print(a)   