# list comprehension =  a way to meake a new list with less syntex 
                    #    can mimic certain lambda functions, easier to read
                    # list=[expression for item in iterable]
                    
square=[]
for i in range (1,11):
    square.append(i*i)           # normal way of making a list
print(square)

square=[i*i for i in range(1,11)]
print(square)                          # list comprehension 


# one more example
students=[100,90,80,70,60,50,40,30,0]
# passed_student=list(filter(lambda x:x>=60,students))
passed_student=[i if i>=60 else "failed" for i in students]
print(passed_student)