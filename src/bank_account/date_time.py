class DateTime:
    def __init__(self, d, t) -> None:
        self.__date = d
        self.__time = t
        
    def __str__(self):
        return f"{self.__date} {self.__time}"

    def get_time(self):
        return self.__time
    
    def get_date(self):
        return self.__date
    
"ccc"

