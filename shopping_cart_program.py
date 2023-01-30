# shopping cart program

# foods=[]
# prices=[]
# total=0

# while True:
#     food=(input("enter the food(q to quit)"))
    
#     if food.lower()=="q":
#         break
#     else:
#         price=float(input(f"enter price of {food}:$"))
#         foods.append(food)
#         prices.append(price)

# for food in foods:
#     print(food, end="")

# for price in prices:
#     total+=price

# print()

# print("---------your cart------------")
# print(foods)
# print(f"your totle is ${total}")

# books shopping cart---------------------------------------------------------------------------------

books=[]
prices=[]
total=0

while True:
    book=input("enter the book(q to quit")
    price=float(input("enter price"))

    if book.lower()=="q":
        break
    else:
        books.append(book)
        prices.append(price)

for price in prices:
    total+=price

print("--------library----------")
print(f" your books {books}",end="")
print(f"your totle is ${total}")