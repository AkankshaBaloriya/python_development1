# multiple inheritance = when a child class is derived from more than one parent class

class prey:

    def flee(self):
        print("this animal flees")

class predator:

    def hunt(self):
        print("this animal is hunting")

class rabbit(prey):
    pass
class hawk(predator):
    pass
class fish(prey,predator):
    pass

Rabbit=rabbit()
Hawk= hawk()
Fish=fish()

Rabbit.flee()
Hawk.hunt()
Fish.flee()
Fish.hunt()