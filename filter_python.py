# filter() =create a colection of elements from an iterable for which a function returns
# 
# filter(function,iterable)

friends=[("rachel",19),
         ("rose",18),
         ("chandler",16),
         ("joey",14),
         ("monica",20)]

drink=lambda x:x[1]>=18

age=list(filter(drink,friends))

for i in age:
    print(i)