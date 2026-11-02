# bank acc == owner, acc n.o, balance, history/statement
from datetime import date, datetime


class Client:
    def __init__(self, names: str, kra_pin: str, dob: str, gender: str):
        self.names = names
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender

    def print_details(self):
        print(self.names)
        print(self.kra_pin)

    def calc_age(self):
        today = date.today()
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        age = today.year - birth_date.year
        return age


class BankAccount:
    def __init__(self, owner: Client, acc_no: str, balance: int):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += abs(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= abs(amount)

    def print_details(self):
        print(self.owner.names)
        print(self.acc_no)
        print(self.balance)
        print("-----------------")


jane = Client("Jane Mwangi", "A001", "1999-10-19", "F")
ahmed = Client("Ahmed Muhamudd", "A002", "2005-10-25", "M")

acc1 = BankAccount(jane, "010101", 70_000)
acc2 = BankAccount(jane, "010102", 45_632)
acc3 = BankAccount(ahmed, "989893", 100_000_000)

acc1.deposit(10_000)
acc2.deposit(20_000)
acc1.print_details()

acc1.withdraw(15_000)
acc1.print_details()

print("Jane's Age", jane.calc_age())
print("Ahmed's Age", ahmed.calc_age())

print(acc1.owner.names, acc1.owner.calc_age())
print(ahmed.names, ahmed.calc_age())

# dob = "18-01-2004"  # d.m.Y
#
# today = date.today()
# print(today)
# print(f"{today.day}/{today.month}/{today.year}")
#
# # convert string to date
# birth_date = datetime.strptime(dob, "%d-%m-%Y")
#
# age = today.year - birth_date.year
# print(age)
