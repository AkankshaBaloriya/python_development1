# sort python

# sort() method = used with lists.
#  sorted() function = used with iterables

a=["harry","styles","john","sena"]

a.sort()
for i in a:                   #sort method in lists
    print(i)
print()
    
#sort in tuple

a=("taylor","swift","justin","timberline")

a=sorted(a,reverse=True)                             #here its sorting in iterables,and also reverse method to reverse it
for i in a:
    print(i) 
print()   

# few more examples

b=[("akki","e",20),
   ("tanu","c",23),
   ("aash","b",18),
   ("bipe","a",12)]

# b=sorted(b)            #to sort it by names
# print(b)
#  b.sort()               #or di it this way
# print(b)

c=lambda x :x[1] # x:x[2]  = for numbers
b.sort(key=c)                         #if you wanna do it with sort method
# c=sorted(b,key=c)            if you wanna do it with sorted function

for i in b:
    print(i)

