items={"popcorn":4.0,
       "juice":3.0,
       "sandwitch":5.0}

order=[]
total=0


for key, value in items.items():
    print(f"{key}: ${value:.3f}")
print("--------------------------------------------")

while True:
    a= input("enter your order").lower()
    if a=="q":
        break
    elif items.get(a) is not None:
        order.append(a)
print(order)

for a in  order:
    total +=items.get(a)
    print(a, end=" ")
print()
print(f"total is ${total:.2f}")

# shopping item
items={"apple":2.1,
       "banana":3.1,
       "watermelon":5.1,
       "pitch":3.1}

order=[]
total=0

for key, value in items.items():
    print(f"{key}: ${value:.3f}")
print("----------------------------------")
    
while True:
    enter=input("enter items here").lower()
    if enter=="q":
        break
    elif items.get(enter) is not None:
        order.append(enter)
print(order)

for a in order:
    total+=items.get(a)
    print(f"total is {total}")