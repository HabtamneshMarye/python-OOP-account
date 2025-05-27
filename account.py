class Account:
    interest_rate = 0.05  # 5% interest

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        self.frozen = False
        self.min_balance = 0
        self.closed = False

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if self.frozen or self.closed:
            return "Account is frozen or closed."
        if amount <= 0:
            return "Deposit amount must be positive."
        self.deposits.append(amount)
        self.balance += amount
        return f"Confirmed: You have received {amount}. Your new balance is {self.balance}"

    def withdraw(self, amount):
        if self.frozen or self.closed:
            return "Account is frozen or closed."
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if self.balance - amount < self.min_balance:
            return "Insufficient funds or below minimum balance."
        self.withdrawals.append(amount)
        self.balance -= amount
        return f"Confirmed: You have withdrawn {amount}. Your new balance is {self.balance}"

    def transfer_funds(self, amount, other_account):
        if self.frozen or self.closed or other_account.closed:
            return "Cannot transfer from/to a frozen or closed account."
        if amount <= 0 or self.balance - amount < self.min_balance:
            return "Invalid amount or insufficient balance."
        self.withdraw(amount)
        other_account.deposit(amount)
        return f"Transferred {amount} to {other_account.name}."

    def request_loan(self, amount):
        if self.frozen or self.closed:
            return "Cannot request loan. Account is frozen or closed."
        if amount <= 0:
            return "Loan amount must be positive."
        self.loan += amount
        self.deposit(amount)
        return f"Loan of {amount} granted. Your loan balance is now {self.loan}."

    def repay_loan(self, amount):
        if amount <= 0:
            return "Repayment must be positive."
        if self.balance < amount:
            return "Insufficient balance to repay loan."
        repayment = min(amount, self.loan)
        self.loan -= repayment
        self.balance -= repayment
        return f"Repayment of {repayment} made. Remaining loan balance is {self.loan}."

    def view_account_details(self):
        return (
        f"Account Owner: {self.name}\n"
        f"Balance: {self.balance}\n"
        f"Loan Balance: {self.loan}\n"
        f"Account Frozen: {self.frozen}\n"
        f"Account Closed: {self.closed}\n"
        f"Deposits: {self.deposits}\n"
        f"Withdrawals: {self.withdrawals}\n"
    )

  