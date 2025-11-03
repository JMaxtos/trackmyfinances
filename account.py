import csv
import os
from datetime import datetime

# Financial account with a name, balance, and a CSV file that stores the account’s balance and transaction history.
class Account :

    # Initialize a new Account instance
    def __init__(self,account_name,balance = 0):

        # Store account name 
        self.account_name = account_name
        
        # Check if the accounts directory is created
        ACCOUNT_DIR = "Accounts"
        if not os.path.exists(ACCOUNT_DIR):
            os.makedirs(ACCOUNT_DIR)

        # Create account CSV file on accounts directory
        self.file = os.path.join(ACCOUNT_DIR, f"{self.account_name}.csv")


        # Check if account already exists
        if self.findAccount(self.account_name):
            # Load balance for existing account
            self.loadBalance()
        else:
            # Add provided balance and create CSV file
            self.balance = balance
            self.createCSVFile()
    
    
    # Return the current balance of the account
    def getBalance(self):
        # Refresh balance to ensure the value is up-to-date
        self.loadBalance()
        return self.balance

    # Check if an account file with the given name exists
    @staticmethod
    def findAccount(name):
        file = os.path.join("accounts", f"{name}.csv")
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
        try:
        # Open file in binary to move cursor to the end
            with open(self.file, 'rb') as f:

            # Set cursor 2 bytes before the end of file
                f.seek(-2, os.SEEK_END)
                
                # Move cursor behind until it founds '\n'
                while f.read(1) != b'\n':
                    f.seek(-2, os.SEEK_CUR)

                # Read line once found '\n' and convert to string
                last_line = f.readline().decode()
            
            # Get last value
            *_, balance = last_line.strip().split(',')

            # Convert balance in float
            self.balance = float(balance)

        except Exception:
            self.balance = 0