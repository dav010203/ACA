class Length:
    lens = {"meter": 1, "feet": 3.28, "km": 1000.0, "yard": 1.09, "mile": 1609.344}

    def __init__(self, length, point) -> None:
        self.__length = length
        self.__point = point

    @property
    def length(self) -> float:
        return self.__length
    
    @length.setter 
    def length(self, val) -> None:
        self.__length = val

    @property 
    def point(self) -> str:
        return self.__point

    @point.setter
    def point(self, val) -> None:
        self.__point = val

    def __add__(self, other):
        if self.point == other.point:
            length = self.length + other.length
            return Length(length, self.point)
        else:
            length = self.length * self.lens[self.point] + other.length * other.lens[other.point]
            return Length(length, 'meter')
            
    
    def __str__(self) -> str:
        if self.point == 'meter':
            return "{} {}".format(self.length, self.point)
        else:
            return "{} {}".format(self.length * self.lens[self.point], 'meter')
        
l1 = Length(1000, "feet")
l2 = Length(2, "feet")
l3 = l1 + l2
print(l3)