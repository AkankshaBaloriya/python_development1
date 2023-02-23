# map() = applies function to each item in an iterable(lists,tuples,etc.)
# 
# map(function,iterable)

store=[("harry",20.00),
       ("perry",50.00),
       ("jerry",70.00),
       ("carry",10.00)]

func=lambda x: (x[0],x[1]*0.83)
func1=lambda x: (x[0],x[1]/0.85)

store1=list(map(func,store))
store2=list(map(func1,store))

for i in store1:
    print(i)
print()
for i in store2:
    print(i)