# walrus operator = assignment operator(:=)

# new to python 3.8
# assignment expression = walrus operator
# assigns values to variables as part of a larger expression

a="akki"
print(a)      # normal way 

print(a:="akki")       # walrus operator


foods=list()
while True:
    food=input("enter food here") #normal way
    if food =="q":
        break
    foods.append(food)

foods=list()
while food:= input("enter food") !="q":        #walrus method
    foods.append(food)

