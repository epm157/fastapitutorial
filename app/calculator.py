
def add(num1, num2):
    return num1 + num2


class BalanceException(Exception):
    pass

class BankAccount():
    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise BalanceException("Insufficient balance")
        self.balance -= amount

    def collect_interest(self):
        self.bala *= 1.1
































