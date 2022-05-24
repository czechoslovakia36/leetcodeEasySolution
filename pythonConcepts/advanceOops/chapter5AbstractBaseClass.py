 

from abc import ABC,abstractmethod
# abstact base class
class GraphicShapes:
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicShapes):
    def __init__(self,radius):
        self.radius=radius
    def calcArea(self):
        return 3.14*self.radius*self.radius

class Square(GraphicShapes):
    def __init__(self,side):
        self.side=side

    def calcArea(self):
        return self.side*self.side

# g=GraphicShapes()
        

c=Circle(10)
print(c.calcArea())
s=Square(12)
print(s.calcArea())
