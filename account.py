
class Transaction:
    def __init__(self, amount, narration, transaction_type):
        self.date_time = datetime.now()
        self.amount = amount
        self.narration = narration
        self.transaction_type = transaction_type 

    def __str__(self):
        return f"{self.date_time} | {self.transaction_type.upper()} | {self.narration} | Amount: {self.amount}"

class Account:
    interest_rate = 0.05 

    def __init__(self, name):
        self.name = name
        self.balance=0
        self.transactions = []
        self.loan = 0
        self.frozen = False
        self.min_balance = 0
        self.closed = False

    def get_balance(self):
        balance = 0
        for check in self.transactions:
            if check.transaction_type in ["deposit", "loan", "interest"]:
                balance += check.amount
            elif check.transaction_type in ["withdrawal", "repayment", "transfer_out"]:
                balance -= check.amount
        return balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.transactions.append(Transaction(amount, "Deposit made", "deposit"))
        return f"Confirmed: You have received {amount}. Your new balance is {self.get_balance()}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if self.get_balance() - amount < self.min_balance:
            return "Insufficient funds or below minimum balance."
        self.transactions.append(Transaction(amount, "Withdrawal made", "withdrawal"))
        return f"Confirmed: You have withdrawn {amount}. Your new balance is {self.get_balance()}"

    def transfer_funds(self, amount, other_account):
        if amount <= 0:
            return "Invalid amount or insufficient balance."
        self.transactions.append(Transaction(amount, f"Transfer to {other_account.name}", "transfer_out"))
        other_account.transactions.append(Transaction(amount, f"Transfer from {self.name}", "deposit"))
        return f"Transferred {amount} to {other_account.name}."

    def request_loan(self, amount):
        if amount <= 0:
            return "Loan amount must be positive."
        self.loan += amount
        self.transactions.append(Transaction(amount, "Loan granted", "loan"))
        return f"Loan of {amount} granted. Your loan balance is now {self.loan}."

    def repay_loan(self, amount):
        if amount <= 0:
            return "Repayment must be positive."
        if self.get_balance() < amount:
            return "Insufficient balance to repay loan."
        repayment = min(amount, self.loan)
        self.loan -= repayment
        self.transactions.append(Transaction(repayment, "Loan repayment", "repayment"))
        return f"Repayment of {repayment} made. Remaining loan balance is {self.loan}."

    def view_account_details(self):
        return f"Account Owner: {self.name}\n Balance: {self.get_balance()}"

    def change_account_owner(self, new_name):
        self.name = new_name
        return f"Owner name updated {self.name}"

    def account_statement(self):
        print("Account Statement:")
        for transaction in self.transactions:
            print(transaction)
        print(f"Current Balance: {self.get_balance()}")

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        if interest > 0:
            self.transactions.append(Transaction(interest, "Interest applied", "interest"))
        return f"Interest of {interest} applied"
        return "No interest applied"

    def freeze_account(self):
        self.frozen = True
        return "Account frozen"

    def unfreeze_account(self):
        self.frozen = False
        return "Account unfrozen"

    def set_minimum_balance(self, amount):
        if amount >= 0:
            self.min_balance = amount
            return f"Minimum balance set to {amount}"
        return "Invalid minimum balance"

    def close_account(self):
        self.closed = True
        return "Account closed"
