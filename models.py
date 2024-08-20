# models.py

class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

class Transaction:
    def __init__(self, source_account_number, destination_account_number, amount):
        self.source_account_number = source_account_number
        self.destination_account_number = destination_account_number
        self.amount = amount
