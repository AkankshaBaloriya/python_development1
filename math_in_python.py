# arithomatic operators/built in math function/math functions

#  arithomatic operators
# { + , - , * , / ,** ,%}
friend=2
# friends=fri+1    (instead of this we can also do the way given below)
friend+=2

print(friend)

# {-}
apple=14
apple-=5
print(apple)

# {*}
b=4
b*=3
print(b)

# {/}
c=10
c/=2
print(c)

# **(times)(exponantials)
n=3
n**=3
print(n)

# %(remainder)(marguals)
g=20
g%=3
print(g)

# math related built in function{round/absolute/ power/max/min}-------------------------------------------
x=2.7
y=4
z=2

# round
# result=(round(x)){this is to do but we can also do direct print mathod}
print(round(x))
# absolute
print(abs(x))
# power
print(pow(2,5))
# min
print(min(x,y,z))
# max
print(max(x,y,z))

# external operators(ex. import math) (math module)
# operators(pi , e ,square root funcion ,ceil ,floor)
import math

x=9.9

print(math.pi)
print(math.e)
print(math.sqrt(x))
print(math.ceil(x))#round to hightest of given number
print(math.floor(x))#round to lowest of given number

# practice of math operator------------------------------------------------------------------------------------
# do a "c=2 pi r"

radius=float(input("enter radius(r"))
c=2 * math.pi * radius
print(round(c))

# now do a "a=pi square"                                                                                                                                                 
r=float(input("enter radius again"))

a=math.pi* pow(r,2)
print(f"here is radius{a}!")
