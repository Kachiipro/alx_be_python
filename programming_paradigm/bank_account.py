class BankAccount:
    def __init__(self, account_balance=0):
        self.account = account_balance

    def deposit(self, amount):
        self.account += amount

    def withdraw(self, amount):
        if self.account < amount:
            return False
        else:
            self.account -= amount

            return True

    def display_balance(self):
        print(f"Current Balance:${self.account}.00")
