import csv
import os
from datetime import datetime

# Financial account with a name, balance, and a CSV file that stores the account’s balance and transaction history.
class Account :

    # Initialize a new Account instance
    def __init__(self,account_name,balance = 0):

        # Store account name and file
        self.account_name = account_name
        self.file =f"{self.account_name}.csv"

        # Check if account already exists
        if self.findAccount(self.account_name):
            # Load balance for existing account
            self.loadBalance()
        else:
            # Add provided balance and create CSV file
            self.balance = balance
            self.createCSVFile()
    
    
    # Returns the current balance of the account
    def getBalance(self):
        # Refresh balance to ensure the value is up-to-date
        self.loadBalance()
        return self.balance

    # Check if an account file with the given name exists
    @staticmethod
    def findAccount(name):
        file = f"{name}.csv"
        return os.path.isfile(file)
    
    # Create the CSV file 
    def createCSVFile(self):
       with open(self.file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
        
        # Write headers for transactions (consistent structure)
            writer.writerow(['Date', 'Type', 'Category', 'Value', 'Balance'])

        # Add initial transaction line representing the starting balance
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'Income',
                'Initial Amount',
                self.balance,
                self.balance
        ])
    
    # Loads the latest balance by reading the last line of the CSV file
    def loadBalance(self):
       with open(self.file, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # skip header line

        # Read all lines and get the last one (latest transaction)
        rows = list(reader)

        if len(rows) > 0:
            last_row = rows[-1]
            try:
                # Current Balance
                self.balance = float(last_row[-1])  
            except (ValueError, IndexError):
                # Corrupted file, default balance = 0
                self.balance = 0
        else:
            # Empty file besides header
            self.balance = 0
