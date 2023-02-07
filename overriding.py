
class animal:

    def eat(self):
        print("this animal is eating")

class rabbit(animal):
    pass

    def eat(self):
        print("this rabbit is eating a carrot")

Rabbit=rabbit()
Rabbit.eat()