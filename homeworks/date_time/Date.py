import datetime as dt
x = dt.datetime.now()

class DateError(Exception):
    def __init__(self, msg, val):
        self.__message = "{} value out of range".format(msg)
        self.__value = val 
        
    def get_message(self):
        return self.__message
        
    def get_value(self):
        return self.__value

class Date:
    MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def __init__(self, y, m, d):
        try:
            if y < 0:
                raise DateError("Year", y)
            if m < 0 or m > 12:
                raise DateError("Month", m)
            if d < 0 or d > self.MONTH_DAYS[m]:
                raise DateError("Day", d)
        except DateError as err:
            print(err)
        else:
            self.__year = y 
            self.__month = m 
            self.__day = d 
    
    def __str__(self):
        params = ("0" + str(i) if i < 10 else i for i in [self.__year, self.__month, self.__day])
        return "{}/{}/{}".format(*params)
        
    def get_year(self):
        return self.__year
    
    def get_month(self):
        return self.__month
    
    def get_day(self):
        return self.__day

    
    def add_year(self, y):
        self.__year += y
        
    def add_month(self, m):
        x = self.__month + m

        while x > 12:
            x -= 12
            self.add_year(1)
        self.__month = x        

    def add_day(self, d):
        x = self.__day + d
        while x > self.MONTH_DAYS[self.__month]:
            x -= self.MONTH_DAYS[self.__month]
            self.add_month(1)
        self.__day = x
        
d = Date(x.year, x.month, x.day)


