class cars:
     
    wheels=4          # class variable = varible which is inside the class but outside the object constructor
    
    def __init__(self,make,modal,year,color):    # object constructor
     self.make=make                           # instance variable
     self.modal=modal
     self.year=year              # attributes
     self.color=color

