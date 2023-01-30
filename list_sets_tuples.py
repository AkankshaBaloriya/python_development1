# lists, sets. tuples(this are used to store multiple values)

# lists= [] ordered and changable.Duplicates OK
# set= {} unordered and immutable, but add/remove OK. NO duplicates
# tuples=() orderd and unchangable.Duplicate OK. FASTER

# lists---------------------------------------------------------------------------------------------------

fruits=["apple", "banana", "orange", "coconut"]
# print(type(fruits))   #(code to get to know what class is this)
print(fruits[::-2]) #to print in reverse

for fruit in fruits:
    print(fruit)
#here used "for loop" to get the each values in different row

# methods for list(dir, len, in, append, remove, help, remove, insert, sort, reverse, clear, index, count, )

print(dir(fruits))# "dir" method is used to see what other methods are available for this variable or list etc.

# print(help(fruits))      #"help" method will show the detail of each method that can be used in thar variable,list etc.

print(len(fruit))# "len" is used to see the lenth of the variable values

print("apple" in fruits)# "in" is used to see weather apple is in values of variable or not

# fruits=["apple"]#duplicate can be kept
fruits[2]="pineapple"#to replace no.2 value with pineaplle
print(fruits)

fruits.append("strawberry")# to append new value
print(fruits)

fruits.remove("apple")#to remove any value
print(fruits)

fruits.insert(2,"kiwi")#to insert values
print(fruits)

fruits.sort()#to sort values alphabaticaly
print(fruits)

fruits.reverse()#to reverse the values
print(fruits)

print(fruits.index("kiwi"))#to get to know index number of the value
print(fruits.count("coconut"))#to get to know how many coconuts are their in list,set etc...

print(fruits.clear())

# sets---------------------------------------------------------------------------------------------

vegetables={"bringle", "tomato", "potato", "beans"}
print(vegetables)
print(dir(vegetables))

# methods for sets(in, add, len,help,dir, remove, pop, clear etc...)

# tuples---------------------------------------------------------------------------------

names=("akki", "tanu", "aash", "priyanka","raj")

# methods for tuples(index, count)
