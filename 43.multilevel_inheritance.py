# multilevel inheritance = when a derived (child) class inherits another derived (child) class

class Organism:
    
    alive=True

class animal(Organism):

    def eat(self):
        print("this animal is eating")

class Dog(animal):

    def bark(self):
        print("this dog is barking")

dog=Dog()
print(Dog.alive)
dog.eat()
dog.bark()
