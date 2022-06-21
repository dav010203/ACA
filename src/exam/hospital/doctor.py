from datetime import date, datetime
from patient import Patient

class Doctor:
    def __init__(self, name, surname) -> None:
        self.__name = name
        self.__surname = surname
        self.__schedule = {}
    
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
    def schedule(self):
        return self.__schedule
    
    def is_registered(self, patient) -> bool:
        for i in self.schedule.values():
            if not i != patient:
                return False
        return True

    def is_free(self, datetime) -> bool:
        k = datetime.strftime("%x")+ " " + datetime.strftime("%X")
        if k in self.schedule:
            return False
        return True

    def register_patient(self, patient, datetime):
        k = datetime.strftime("%x")+ " " + datetime.strftime("%X")
        if self.is_free(datetime) and self.is_registered(patient):
            self.schedule[k] = patient
        else:
            print("Datetime {} already taken from {} patient".format(k, self.schedule[k]))

        

    def __repr__(self) -> str:
        pass

d1 = datetime(2022, 6, 21, 13, 30)
p1 = Patient("Davit", "Simonyan", 20, "M")
p2 = Patient("Eduard", "Babayan", 20, "M")


dr = Doctor("Artash", "Zakaryan")
dr.register_patient(p1, d1)
# print(dr.schedule)
# dr.register_patient(p2, d1)
# print(dr.schedule)
print(dr.is_free(datetime(2022, 6, 21, 13, 30)))
dr.register_patient(p1, d1)