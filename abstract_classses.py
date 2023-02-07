# prevents a user from creating an object of that class 
#  + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation

from abc import abc, abstractmethod
class vehicle:
    
    @abstractmethod
    def go(self):
        pass

class car(vehicle):

    def go (self):
        print("you drive the car")

class motorcycle(vehicle):
    def go(self):
        print("you ride the motorcycle")

Vehicle=vehicle()
Car= car()
Motorcycle= motorcycle()

Vehicle.go()
Car.go()
Motorcycle.go()