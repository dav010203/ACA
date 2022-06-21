class Length:
    lens = {"meter": 1, "feet": 3.28, "km": 1000.0, "yard": 1.09, "mile": 1609.344}

    def __init__(self, length, point) -> None:
        self.__length = length
        self.__point = point

    @property
    def length(self):
        return self.__length
    
    @property 
    def point(self):
        return self.__point

    @length.setter
    def length(self, val):
        self.__length = val

    @point.setter
    def point(self, val):
        self.__point = val

    def __add__(self, other):
        if self.point == other.point:
            length = self.length + other.length
            return Length(length, self.point)
        else:
            length = self.length * self.lens[self.point] + other.length * self.lens[other.point]
            return Length(length, 'meter')
            
    
    def __str__(self):
        if self.point == 'meter':
            return "{} {}".format(self.length, self.point)
        else:
            return "{} {}".format(self.length * self.lens[self.point], 'meter')
        
l1 = Length(1000, "feet")
l2 = Length(2, "meter")
l3 = l1 + l2
print(l3)