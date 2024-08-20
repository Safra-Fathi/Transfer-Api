# services.py
from models import Account, Transaction

class TransferService:
    def __init__(self):
        # This will store accounts in memory (like a simple database)
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0.0):
        if account_number in self.accounts:
            raise ValueError("Account already exists!")
        self.accounts[account_number] = Account(account_number, initial_balance)

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer(self, transaction):
        source_account = self.get_account(transaction.source_account_number)
        destination_account = self.get_account(transaction.destination_account_number)

        if not source_account or not destination_account:
            return "One or both accounts do not exist."
        
        if source_account.balance < transaction.amount:
            return "Insufficient funds."
        
        # Perform the transfer
        source_account.balance -= transaction.amount
        destination_account.balance += transaction.amount
        
        return "Transfer successful."
