class Patient:
    def __init__(self, name, surname, age, gender) -> None:
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__gender = gender

    @property 
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, val):
        self.__name = val

    @property 
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self, val):
        self.__surname = val
    
    @property 
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, val):
        self.__age = val
    
    @property 
    def gender(self):
        return self.__gender
    
    @gender.setter
    def gender(self, val):
        self.__gender = val

    def __ne__(self, other) -> bool:
        if self.name == other.name and self.surname == other.surname and self.age == other.age and self.gender == other.gender:
            return False
        return True

    
    def __repr__(self) -> str:
        return "{} {} - {}, {} years old.".format(self.name, self.surname, self.gender, self.age)