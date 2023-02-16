# while loop
# name program---------------------------------------

name=input("enter your name")

while name=="":
    print("type name first")
    name=input("enter your name")

print(f"hello{name}")

# age program0-----------------------------------------

age=int(input("enter the age"))

while not age>0:  #not logical operator can be use here
    print("age cant be in negative")
    age=int(input("enter the age"))

print(age)

# food program

food=input("enter the food")

while not food=="q":
    print(f"your food is {food}")
    food=input("enter the food")

print("bye")

# number--------------------------------------------

number=int(input("enter the number"))
while not number<1 and number>6:
    print("wrong guess")
    number=int(input("enter the number"))

print(f"your guess {number} is currect")