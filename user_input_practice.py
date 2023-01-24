# # mad libs game(story)-----------------------------------------------------------------------------

noun=input("Enter first noun")
noun2=input("Enter noun")
adjective=input("Enter adjective")
verb=input("Enter verb")

print(f"my name is {noun} and what is your name")
print(f"i am {adjective} and you?")
print(f"i live in {noun2}")
print(f"i do {verb} there")

# # area calculation of a ractangle------------------------------------------------------------------------

length=int(input("enter length"))
width=int(input("enter width"))

area= length * width
print(area)

# shopping cart program------------------------------------------------------------------------------------

item=input("enter item you bought")
price=float(input("what is the price"))
quantity=int(input("how many do you want"))

total= price*quantity

print(f"your totle is ${total} !")