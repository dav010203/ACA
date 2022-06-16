from person import Person
from money import Money
from date_time import DateTime
from random import randint
from datetime import datetime as dt

class BankAccount:
    def __init__(self, p : Person, m: Money, d: DateTime) -> None:
        self.__customer = p
        self.__account_number = ""
        for i in range(16):
            self.__account_number += str(randint(0, 9))
        self.__balance = m 
        self.__balance_start = d
        x = d.get_date().split("/")
        if int(x[2]) < 10:
            self.__valid_till = f"{x[0]}/{x[1]}/{x[2][0]}{int(x[2][1]) + 3} {d.get_time()}"
        else:
            self.__valid_till = f"{x[0]}/{x[1]}/{int(x[2]) + 3} {d.get_time()}"


    def __str__(self):
        return f"({self.__account_number}) - {self.__customer.get_full_name()}, {self.__customer.get_birthday()}, {self.__customer.get_email()}, {self.__customer.get_phone_number()} | {self.__balance} | {self.__balance_start} valid till - {self.__valid_till}"

    def deal(self, m: Money):
        if m.amount < self.__balance.amount:
            self.__balance -= m

    def fill_balance(self, m: Money):
        self.__balance += m

    def deposite(self, m: Money, d):
        if self.__balance.currency == 'AMD':
            p = 8
        else:
            p = 4
        
        if m.amount <= self.__balance.amount:
            self.__balance.amount -= m.amount

            for _ in range(d):
                m.amount *= (1 + p / 100)
            
            self.__balance += m
        else:
            print("You have not enough money to make a deposit, please fill your balance or choose another amount")

        
b1 = BankAccount(Person("Davit Simonyan", "2001/09/14", "Male", "davidsimonyan460@gmail.com", "+37491464610"), Money("USD", 2000), DateTime(dt.now().strftime("%x"), dt.now().strftime("%X")))
        

print(b1)

b1.deal(Money("EUR", 850))
print(b1)
b1.deposite(Money("AMD", 200000), 10)
print(b1)



