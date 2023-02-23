# class variable in python

from class_variables import cars

cars_1=cars("chevy","corette",2023,"blue")
cars_2= cars("ford","mustang",2019,"red")

cars_1.wheels=2

print(cars_1.wheels)
print(cars_2.wheels)
# print(Car.wheels)