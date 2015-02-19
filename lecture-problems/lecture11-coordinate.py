class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def distance(self,other):
        return ((self.getX() - other.getX()) ** 2 + 
                    (self.getY() + other.getY()) ** 2) ** 0.5
        
    def __eq__(self, other):
        # First make sure `other` is of the same type 
        assert type(other) == type(self)
        # Since `other` is the same type, test if coordinates are equal
        return self.getX() == other.getX() and self.getY() == other.getY()
        
    def __repr__(self):
        return 'Coordinate(%d, %d)' % (self.getX(), self.getY())


c = Coordinate(3,4)
Origin = Coordinate(0,0)