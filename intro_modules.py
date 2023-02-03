# module =   a file containing code you want to include in your program use "import" to include a module     (built in or your own) useful to break up a large program reusable seperate files.

# print(help("modules"))

# import math  #----------------------------------(0)

# print(math.pi)

# # different ways to import modules

# # import math as m-----------------------------(1)

# # from math import pi-----------------------------(2)

# a, b, c, d =1, 2, 3, 4


# print(math.e ** a)
# print(math.e ** b)
# print(math.e ** c)
# print(math.e ** d)

import example

result = example.pi
result=example.square(3)
result=example.cube(3)
result=example.circumference(3)
result=example.area(3)

print(result)