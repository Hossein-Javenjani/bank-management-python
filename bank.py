from account import Account


class Bank:
    def __init__(self):
        self.accounts = []

    def create(self):
        owner = input("inter name : ")
        while True:
            try:
                account_number = int(input("inter account number : "))
            except ValueError:
                print("account number must be a int number!")
                continue
            if any(i.account_number == account_number for i in self.accounts):
                print("This account number has already been used!")
                continue
            break 

        while True:
            try:
                balance = float(input("inter balance : "))
                break
            except ValueError:
                print("balance must be a number!")

        account = Account(owner, account_number, balance)
        self.accounts.append(account)

    def deposit(self):
        while True:
            try:
                account_number = int(input("What account do you want to deposit money into? "))
                break
            except ValueError:
                print("Account number must be a number!")
        found = False
        for i in self.accounts:
            if account_number == i.account_number:
                add_balance = float(input("How much money do you want to deposit? "))
                i.balance += add_balance
                found = True
                print("deposited successfully")
                break
        if not found:
            print(f"{account_number} isn't account in the bank")

    def withdraw(self):
        while True:
            try:
                account_number = int(input("What account do you want to withdraw money into? "))
                break
            except ValueError:
                print("Account number must be a number!")
        found = False
        for i in self.accounts:
            if account_number == i.account_number:
                withdrawing_balance = float(
                    input("How much money do you want to withdraw? ")
                )
                if withdrawing_balance <= i.balance:
                    i.balance -= withdrawing_balance
                    print("withdrawed successfully")
                else:
                    print("Insufficient balance!")
                found = True
                break
        if not found:
            print(f"{account_number} isn't account in the bank")

    def transfer(self):
        while True:
            try :
                transfer_from = int(input("Originating account number?  "))
                break
            except ValueError :
                print("Originating account must be a number!")
        while True:
            try :
                transfer_to = int(input("Destination account number? "))
                break
            except ValueError :
                print("Destination account must be a number!")
        while True:
            try :
                amount = float(input("How much do you want to transfer? "))
                break
            except ValueError :
                print("value amount transfer must be a number!")
        found = False
        for i in self.accounts:
            for j in self.accounts:
                if (
                    transfer_from == i.account_number
                    and transfer_to == j.account_number
                ):
                    if amount <= i.balance:
                        i.balance -= amount
                        j.balance += amount
                        print("transfer successfully!")
                    else:
                        print("Insufficient balance!")
                    found = True
                    break
        if not found:
            print(f"{transfer_from} or {transfer_to} aren't account in the bank")

    def show_account(self):
        if len(self.accounts) == 0:
            print("There is no account.")
        else:
            for num, account in enumerate(self.accounts, start=1):
                print(f'{"=" * 10} Account {num} {"=" * 10}\n {account}\n{"=" * 30}')

    def search_account(self):
        get_name = input("name owner : ").strip().lower()
        found = False
        for i in self.accounts:
            if get_name == i.owner.lower():
                print(f"{"=" * 10} owner found {"=" * 10}\n{i}")
                found = True
                break
        if not found:
            print(f"{get_name} does not have an account in this bank!")

    def save(self):
        with open("bank.txt", "w") as bank_file:
            for i in self.accounts:
                bank_file.write(f"{i}\n{'=' * 20}\n")
            print("Data saved successfully!")

    def load(self):
        with open("bank.txt", "r") as bank_file:
            return print(bank_file.read())
