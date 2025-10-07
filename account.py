import csv
import os
from datetime import datetime

# Account class representes a financial account
# with a name, balance, and an associated CSV file
# to store transactions.

class Account :
    def __init__(self,account_name,balance = 0):
        self.account_name = account_name
        self.file =f"{self.account_name}.csv"

        if self.findAccount(self.account_name):
            self.loadBalance()
        else:
            self.balance = balance
            self.createCSVFile()
    
    
    # Returns the current balance of the account
    def getBalance(self):
        self.loadBalance()
        return self.balance

    @staticmethod
    def findAccount(name):
        file = f"{name}.csv"
        return os.path.isfile(file)
    
    # Create the CSV file 
    def createCSVFile(self):
       with open(self.file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # Balance written on the first Line
            writer.writerow(['Balance', self.balance])
            # Index of Transactions
            writer.writerow(['Date', 'Type', 'Category', 'Value'])
    
    
    def loadBalance(self):
       # Reads first CSV Line
        with open(self.file, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            first_line = next(reader)
            if first_line[0].lower() == 'balance':
                self.balance = float(first_line[1])
            else:
                # CSV corromped equals balance = 0
                self.balance = 0
