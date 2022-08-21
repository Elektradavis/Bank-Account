class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        else: 
            self.balance = self.balance - amount   
        return self     

    def display_account_info(self):
        print("Balance: " + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

    @classmethod
    def all_balances(cls): 
        for account in cls.all_accounts:
            print(account.balance)


User_1 = BankAccount(0.02, 500)

User_2 = BankAccount(0.04, 200)

User_1 = User_1.deposit(400).deposit(350).withdraw(100).yield_interest().display_account_info()

User_2 = User_2.deposit(200).deposit(400).withdraw(50).withdraw(10).withdraw(20).withdraw(40).yield_interest().display_account_info()

BankAccount.all_balances()