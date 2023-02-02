# default arguments= a default value for certain parameters
        #    default is used when that argument is ommited
        #  make your function more flexible,reduces # of arguments
        #  1.positional, 2.default, 3.keyword, 4. arbitraty
# default arguments

def net_price(price,discount=0,tax=0.03):#discount=0 is called setting default value
    return price*(1-discount)*(1+tax)

print(net_price(100 ,0.2))

# count up timer
import time

def count(end,start=2):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("done!")
count(10,3)