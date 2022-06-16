import datetime as dt
x = dt.datetime.now()

class TimeError(Exception):
    def __init__(self, msg, val):
        self.__message = "{} value out of range".format(msg)
        self.__value = val 
        
    def get_message(self):
        return self.__message
        
    def get_value(self):
        return self.__value
        
class Time:
    def __init__(self, h, m, s):
        try:
            if h < 0 or h > 23:
                raise TimeError("Hour", h)
            if m < 0 or m > 59:
                raise TimeError("Minute", m)
            if s < 0 or s > 59:
                raise TimeError("Second", s)
        except TimeError as err:
            print(err)
        else:
            self.__hour = h 
            self.__minute = m 
            self.__second = s 
        finally:
            print("Object creation process")    
            
    def __repr__(self):
        params = ("0" + str(i) if i < 10 else i for i in [self.__hour, self.__minute, self.__second])
        return "{}:{}:{}".format(*params)
      
    def get_second(self):
        return self.__second
        
    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def input_validation(self, inp):
        try:
            if type(inp) != int:
                raise TypeError
        except TypeError:
            print("Enter a valid input")
            return 0
        else:
            return inp

    def set_hour(self, x):
        if x > 0 and x < 23:
            self.__hour = x
        else:
            print("Sorry: Invalid value")
            
    def add_hour(self, h):
        h = self.input_validation(h)
        self.__hour = (self.__hour + h) % 24
        
    def add_minute(self, m):
        m = self.input_validation(m)
        x = self.__minute + m
        self.__minute = x % 60
        self.add_hour(x // 60)
        
    def add_second(self, s):
        s = self.input_validation(s)
        x = self.__second + s
        self.__second = x % 60
        self.add_minute(x // 60)
                
t = Time(x.hour, x.minute, x.second)
