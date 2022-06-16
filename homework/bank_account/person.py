class Person:
    def __init__(self, fn, b, g, m, ph) -> None:
        self.__full_name = fn
        self.__birthday = b
        self.__gender = g
        self.__email = m
        self.__phone_number = ph

    def __str__(self):
        return f"{self.__full_name}, {self.__birthday}"
    
    def get_full_name(self):
        return self.__full_name
    
    def get_birthday(self):
        return self.__birthday
    
    def get_gender(self):
        return self.__gender
    
    def get_email(self):
        return self.__email
    
    def get_phone_number(self):
        return self.__phone_number
    
    def set_email(self, x):
        self.__email = x
    
    def set_phone_number(self, x):
        self.__phone_number = x