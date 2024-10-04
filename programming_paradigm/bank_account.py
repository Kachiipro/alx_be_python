class BankAccount:
    def __init__(self, account):
        self.account = account
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance < amount:
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        print(f"Current Balance: {self.account_balance}")
