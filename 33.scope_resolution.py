# scope of variable and scope resolution

# variable scope------------------------------------------------------------------------------------------
# where a variable is visible and accessible

def a():
    x=1
    print(x)

def b():
    x=2
    print(x)

a()
b()

# scope resolution(legb)--------------------------------------------------------------------------------------------
#  1) local  2) enclosed  3) global  4)Built-in 

# global ------------------------------------
def a():
    print(x)

def b():
    print(x)

x=3         #here we are storing x globally, so x will be accessed by both function a and b

a()
b()

# built in scope------------------------------------

from math import e #this is also a mathod to impoet the built in  module 
def func1():
    print(e)

e=4


func1()

# local----------------------------------------

def a():
    a=7
    print(a)

a()


