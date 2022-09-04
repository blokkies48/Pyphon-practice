class Account:

    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposite_amount):
        self.balance = self.balance + deposite_amount
        return f"Your new balance is ${self.balance}" 

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            return "Not enough monies"

        else:
            self.balance = self.balance - withdraw_amount
            return f"Your new balance is ${self.balance}"

    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: ${self.balance}"
        

acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)

print(acct1.deposit(50))
print(acct1.withdraw(75))
print(acct1.withdraw(500))