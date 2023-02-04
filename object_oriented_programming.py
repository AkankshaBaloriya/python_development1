# python object oriented programming (poop)
# a object contain attributes and methods
# attribte describes what an object is. ex.(name,age,height)
# method is what a object can do. ex(eat,sleep,play,walk etc.)
class Car:

   def __init__(self,make,modal,year,color):    #object constructor
    self.make=make
    self.modal=modal
    self.year=year              # attributes
    self.color=color

   def drive(self):
    print("this"  + self.modal +"car is driving")         # methods

   def stop(self):
    print("this" + self.modal+"car is stopped")