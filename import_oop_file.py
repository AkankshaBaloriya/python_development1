from object_oriented_programming import Car

car_1=Car("chevy","corette",2023,"blue")
car_2= Car("ford","mustang",2019,"red")
print(car_1.make)
print(car_1.modal)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_2.stop()

# second-------------------------------------------------------------------------------------

from object_oriented_programming import human

human_1=human("john","white","curly","male",20)

print(human_1.name)
print(human_1.color)
print(human_1.hairs)
print(human_1.gender)
print(human_1.age)

human_1.work()
human_1.sleep()
