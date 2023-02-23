# 2D lists are list in list

fruit=["apple","banana","grapes","pineapple"]
veg=["potato","bringle","coliflour","ocra"]
names=["ram","shyam","guta","babita"]

group=[fruit,veg,names]
print(group)


print(group[0])
print(group[1][3])

fruit=("apple","banana","grapes","pineapple")
veg=("potato","bringle","coliflour","ocra")
names=("ram","shyam","guta","babita")

group=[fruit,veg,names]
print(group)#we can also create tuple in list or list in tuple or set in list or tuple or vica versa

# use of for loop for this 2D

group=[["apple","banana","grapes","pineapple"],
["potato","bringle","coliflour","ocra"],                     #list in list can also be created this way
["ram","shyam","geeta","babita"]]

for x in group:
    for a in x:
        print(a, end="  ")
        print()


# call dial pad

num_pad=(("1","2","3"),
        ("4","5","6"),
        ("7","8","9"),
        ("*","0","#"))

for x in num_pad:
    for a in x:
        print(a, end=" ")
    print()