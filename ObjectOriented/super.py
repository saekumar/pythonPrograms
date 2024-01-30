#super():Function used to give access to the methods of a parent class.Returns a temporary object of a parent class when used
class Rec:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth


        
class Square(Rec):
    def __init__(self,length,breadth):

        super().__init__(length,breadth)
    def area(self):
        return self.length*self.breadth


class Cube(Rec):
    def __init__(self, length, breadth,height):
        super().__init__(length, breadth)
        self.height=height
    def volume(self):
        return self.breadth*self.height*self.length
square=Square(5,5)
cube=Cube(5,5,5)
print(square.area())
print(cube.volume())