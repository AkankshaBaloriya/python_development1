# suprt() = function used to give access to the method of a parent class. return a temporary object of a parent class when used

class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

class square(rectangle):

    def __init__(self, length,width):
        super().__init__(length,width)

    def area(self):
        return self.length*self.width

class cube(rectangle):

    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height=height

    def volume(self):
        return self.length*self.width*self.height

Square = square(3,3)
Cube = cube(3,3,3)

print(Square.area())
print(Cube.volume())

