import Date
import Time


class DateTime:
    def __init__(self, d, t):
        self.__date = d
        self.__time = t
        
    def __repr__(self):
        return "{} {}".format(self.__date, self.__time)
        
    def add_year(self, y):
        self.__date.add_year(y)
    
    def add_month(self, m):
        self.__date.add_month(m)
        
    def add_day(self, d):
        self.__date.add_day(d)
        
    def add_minute(self, m):
        x = self.__time.get_minute() + m
        hr = 0
        while x > 59:
            hr += 1
            x -= 60
        self.add_hour(hr)
        self.__time.add_minute(x)
        
    def add_second(self, s):
        x = self.__time.get_second() + s
        min = 0
        while x > 59:
            min += 1
            x -= 60
        self.add_minute(min)
        self.__time.add_second(x)
        
    def add_hour(self, h):
        x = self.__time.get_hour() + h
        self.__time.add_hour(h)
        self.__date.add_day(x // 24)

dt = DateTime(Date.d, Time.t)
print(dt)
dt.add_second(3600)
print(dt)
