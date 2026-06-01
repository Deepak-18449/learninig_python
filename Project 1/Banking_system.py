# Smart Banking System
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}, New Balance: {self._balance}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn {amount}, New Balance: {self._balance}")
        else:
            print("Insufficient Balance!")

    def calculate_interest(self):
        raise NotImplementedError("Subclass must implement interest calculation")


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return self._balance * 0.04


class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return self._balance * 0.02

s = SavingsAccount("Ram", 5000)
c = CurrentAccount("Shyam", 8000)
print("Savings Interest:", s.calculate_interest())
print("Current Interest:", c.calculate_interest())