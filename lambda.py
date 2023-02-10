# lambda in python

# lamda function = function writtent in 1 line using lambda keyword
                #   accepts any number of arguments, but pm;y has ome expression.
                #  (think of it as a shortcut)
                # (useful if needed for a short period of time, throw-away) 

# lambda parameters: expression

def duble(x):
    return(x*2)
                            #  normal function
print(duble(2))

# lambda function

double= lambda x: x*3
print(double(5))                 #lambda function

double=lambda x,y : x*y*2
print(double(4,5))

double=lambda first_name,last_name: first_name +"   "+ last_name
print(double("akki","baloriya"))

double= lambda x:True if x>=12 else False
print(double(15))