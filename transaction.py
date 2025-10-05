import os
import csv

class NullValue(Exception):
    pass
class Transaction:
    def __init__(self, account_name):
        self.account_name = account_name
        if self.hasAccountOpen(self.account_name):
            self.expenses = []
            self.transactionMenu()
        else :
            raise NullValue("Account does not Exit")

    def hasAccountOpen(self):
        file =f"{self.account_name}.csv"
        return os.path.isfile(file)
    
    def transactionMenu(self):
        while True:
            print(f'\n Welcome {self.account_name} to Track My Finances')
            print('1. Add an transaction')
            print('2. List all transactions')
            print('3. Show total transactions')
            print('4. Filter transactions by category')
            print('5. Filter transactions by type ')
            print('6. Exit')
    
    
  
            
