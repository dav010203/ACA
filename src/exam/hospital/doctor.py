from datetime import datetime, timedelta
from person import Person
from patient import Patient

class Doctor(Person):
    def __init__(self, name, surname) -> None:
        super().__init__(name, surname)
        self.__schedule = {}

    @property
    def name(self) -> str:
        return super().name

    @property
    def surname(self) -> str:
        return super().surname
    
    @property
    def schedule(self) -> dict:
        return self.__schedule

    def is_registered(self, patient: Patient) -> bool:
        return patient in self.schedule.values()

    def is_free(self, dt: datetime) -> bool:
        dt1 = dt - timedelta(minutes = 30)
        dt2 = dt + timedelta(minutes = 30)

        for d in self.schedule.keys():
            if dt1 < d < dt2:
                return False
        return True

    def register_patient(self, dt: datetime, patient: Patient) -> None:
        if self.is_registered(patient):
            print("patient {} is already registered".format(patient))
        else:
            if self.is_free(dt):
                self.schedule[dt] = patient
            else:
                print("{} is not free".format(dt))

    def __str__(self) -> str:
        result = super().__str__() + "\n"
        for d, p in self.schedule.items():
            result += "{} : {}\n".format(d, p)
        return result[:-1]
    
    

