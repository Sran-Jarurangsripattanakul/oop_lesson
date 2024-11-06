class Account:
    def __init__(self, account_number, account_type, account_name, init_balance):
        self.account_number = account_number
        self.account_type = account_type
        self.account_name = account_name
        self.balance = init_balance

    def deposit(self, amount):
        print(f"Depositing {amount} to {self.account_number}")
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            print(f"Withdrawing {amount} from {self.account_number}")
            self.balance -= amount
        else:
            print(f"Withdrawal amount {amount} exceeds balance of {self.balance} for account {self.account_number}.")

    def show_account(self):
        print(f"Showing details for {self.account_number}")
        print({
            "account_number": self.account_number,
            "type": self.account_type,
            "account_name": self.account_name,
            "balance": self.balance
        })

class AccountDB:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_type, account_name, init_balance):
        if self.search_account(account_number) is None:
            account = Account(account_number, account_type, account_name, init_balance)
            self.accounts.append(account)
            print(f"Account {account_number} created.")
        else:
            print(f"Account {account_number} already exists.")

    def delete_account(self, account_number):
        account = self.search_account(account_number)
        if account:
            print(f"Deleting account: {account.account_number}")
            self.accounts.remove(account)
        else:
            print(f"{account_number} invalid account number; nothing to be deleted.")

    def search_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def deposit(self, account_number, amount):
        account = self.search_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print(f"{account_number} invalid account number; no deposit action performed.")

    def withdraw(self, account_number, amount):
        account = self.search_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print(f"{account_number} invalid account number; no withdrawal action performed.")

    def show_account(self, account_number):
        account = self.search_account(account_number)
        if account:
            account.show_account()
        else:
            print(f"{account_number} invalid account number; nothing to be shown for.")

# Example usage
account_db = AccountDB()
account_db.create_account("0000", "saving", "David Patterson", 1000)
account_db.create_account("0001", "checking", "John Hennessy", 2000)
account_db.create_account("0003", "saving", "Mark Hill", 3000)
account_db.create_account("0004", "saving", "David Wood", 4000)
account_db.create_account("0004", "saving", "David Wood", 4000)

account_db.show_account("0003")
account_db.deposit("0003", 50)
account_db.show_account("0003")
account_db.withdraw("0003", 25)
account_db.show_account("0003")
account_db.delete_account("0003")
account_db.show_account("0003")
account_db.deposit("0003", 50)
account_db.withdraw("0001", 6000)
