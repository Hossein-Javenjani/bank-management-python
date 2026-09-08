class Account:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Owner : {self.owner}\nAccount Number : {self.account_number}\nBalance : {self.balance}"
