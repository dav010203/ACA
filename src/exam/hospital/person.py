class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.__name = name
        self.__surname = surname

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def surname(self) -> str:
        return self.__surname

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    
    @surname.setter
    def surname(self, surname: str) -> None:
        self.__surname = surname
    
    def __str__(self) -> str:
        return "{} {}".format(self.name, self.surname)