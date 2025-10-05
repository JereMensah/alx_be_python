# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional initial balance.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw money if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance in the exact expected format."""
        bal = self.account_balance
        # print as integer if whole number, otherwise show float
        if isinstance(bal, float) and bal.is_integer():
            bal = int(bal)
        print(f"Current Balance: ${bal}")
