# duck typing = concept where the class of an object is less important than the methods class type is not checked if minimummethids/attributes are present "if it walks like a duck. and it quacks like a duck, then it must be a duck"

class Duck:


    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is talking")

class chicken:

    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is talking")

class person:

    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("you caugh it")

duck=Duck()
Chicken=chicken()
Person=person()

Person.catch(Chicken)

