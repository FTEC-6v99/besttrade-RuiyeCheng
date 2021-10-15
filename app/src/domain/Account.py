class Account():
    # create a class that mimics the database table: account
    def __init__(self, account_number, investor_id, balance):
        self.account_number = account_number
        self.investor_id = investor_id
        self.balance = balance
    pass