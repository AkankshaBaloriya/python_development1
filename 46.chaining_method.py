# method chaining = calling multiple method sequentially 
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("ypu start the engin")
        return self

    def drive(self):
        print("you drive the car")
        return self

    def brake(self):
        print("you step on the brakes")
        return self

    def turn_off(self):
        print("you turn off the engine")
        return self

car= Car()
car.turn_on().brake().turn_off()                #thats how we do chaining