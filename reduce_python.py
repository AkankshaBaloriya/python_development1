# reduce() = apply a fy=unction to an iterable and reduce it to a single comulative value.
#            performs function on first two elements and repeats process untill 1 value remains
# 
# reduce(function,iterable)

import functools

letters=["H","e","l","l","o"]
word=functools.reduce(lambda x,y:x+y,letters)
print(word)

num=[1,2,4,3]
num1=functools.reduce(lambda x,y:x*y,num)
print(num1)