class UnknownAtomError(Exception):
    def __init__(self, value):
        self.__value = value 

    def get_info(self):
        return "Invalid atom name - {}".format(self.__value)

class Atom:
    atoms = {"C": "Carbon", "O": "Oxygen", "N": "Nytrogen", "H": "Hydrogen", "P": "Phosphorus"}

    def __init__(self, name):
        try:
            if name not in self.atoms:
                raise UnknownAtomError(name)
        except UnknownAtomError as err:
            self.__is_valid = False
            print(err.get_info())
        else:
            self.__is_valid = True
            self.__name = name    
               
    @property
    def name(self):
        return self.__name
    
    @property
    def is_valid(self):
        return self.__is_valid

    @name.setter
    def name(self, x):
        if x in self.atoms:
            self.__name = x
        else:
            print("Atom does not changed")

    def __add__(self, other):
        return Molecule([self, other])


    def __repr__(self):
        try:
            return self.atoms[self.__name] 
        except AttributeError:
            return "Object is not created"


class Molecule:
    def __init__(self, structure):
        self.__structure = []
        for i in structure:
            if i.is_valid:
                self.__structure.append(i)

    @property
    def structure(self):
        return self.__structure
    
    @structure.setter
    def structure(self, lst):
        self.__structure = lst

    def __add__(self, element):
        res = self.structure
        if isinstance(element, Atom):
            res.append(element)
        else:
            res.extend(element.structure)
        return Molecule(res)

    def __repr__(self):
        res = [i.name for i in self.__structure]
        return "-".join(res)



a1 = Atom("H")
a2 = Atom("O")
a3 = Atom("P")

m2 = Molecule([a3, a1, a2, a3])
m1 = m2 + a1 + a2 + a3 + m2
print(m1)