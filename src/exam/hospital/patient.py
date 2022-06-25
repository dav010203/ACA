from person import Person

class Patient(Person):
    def __init__(self, name: str, surname: str, age: int, gender: str) -> None:
        super().__init__(name, surname)
        self.__age = age
        self.__gender = gender
    
    @property
    def name(self) -> str:
        return super().name
    
    @property
    def surname(self) -> str:
        return super().surname
    
    def __eq__(self, other) -> bool:
        return self is other

    def __str__(self) -> str:
        return super().__str__()
    