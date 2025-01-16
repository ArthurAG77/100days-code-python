"""
day 42 -> Create a class for a bank account with methods for deposit and withdrawal.
https://www.100daysofcode.io/learn/python/day-42
"""

class BankAccount:
    def __init__(self, accountNumber:int, accountOwner:str, accountType:str = 'basic', balance:float = 120.00):
        """
        accountNumber = identifier
        accountOwner = Owner
        accountType = basic, pro or master
        balance: initial ammount
        """
        accountTypes = ['basic', 'pro', 'master']

        self.accountNumber = accountNumber
        self.accountOwner = accountOwner
        self.accountType = accountType.lower() if accountType.lower() in accountTypes else 'basic'
        self.balance = balance
        self.bank_movements = []
        
    def deposit(self, value:float):
        if value > 0:
            self.balance += value
            self.bank_movements.append(f"Deposited $ {value:.2f} -> balance = {self.balance}")
        else:
            print("cann't deposit a value < 0")
    def withdraw(self, value:float):
        if value > 0 and self.balance > value:
            self.balance -= value
            self.bank_movements.append(f"Withdraw $ {value:.2f} -> balance = {self.balance}")
        else:
            print("Cann't withdraw < 0")

    def extract(self):
        for i in self.bank_movements:
            print(i)
    
if __name__ == "__main__":
    conta = BankAccount(1, "Arthur", "Master", 1250.00)
    print(f"{conta.accountOwner}, {conta.accountType}, balance {conta.balance}")
    conta.withdraw(550)
    conta.deposit(50)
    conta.deposit(50)
    conta.extract()
    print(f"Balance: {conta.balance}")
    