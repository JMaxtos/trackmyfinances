import csv
import os
from datetime import datetime
from classes.utils import Utils

# Financial account with a name, balance, and a CSV file that stores the account’s balance and transaction history.
class Account :
    ACCOUNT_DIR = "Accounts"
    # Initialize a new Account instance
    def __init__(self,account_name,balance = 0):

        # Store account name 
        self.account_name = account_name
        
        # Create account CSV file on accounts directory
        self.file = os.path.join(self.ACCOUNT_DIR, f"{self.account_name}.csv")


        # Check if account already exists
        if self.findAccount(self.account_name):
            # Load balance for existing account
            self.loadBalance()
        else:
            # Add provided balance and create CSV file
            self.balance = balance
            self.createCSVFile()
    
    # List all accounts
    @staticmethod
    def listAllAccounts():
        return [f[:-4] for f in os.listdir(Account.ACCOUNT_DIR) if f.endswith('.csv')]  
    
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
    
    # Create the first account when none exists
    @staticmethod
    def createAccount():
            while True:
                user = input("Please insert the name of the new account: ")
                if Account.findAccount(user):
                    print(f'Account name {user} is already in use. Please choose another name.\n')
                else:
                    break 

            while True:
                try:
                    balance = int(input("Account Initial Balance: "))
                    if balance >= 0:
                        break
                    else:
                        print("Sorry, but the initial ammount can't be negative.")
                except ValueError:
                    print("Invalid balance. Please insert a number.")
            try: 
                account = Account(user, balance)
                print("Account Created Successfully")
            except:
                raise Exception("Account couldn't be created")
            return user, account
    

    # Allow user to log in to an existing account
    @staticmethod
    def loginAccount(accounts):
        Utils.clearTerminal()
        while True:
            # Display the current available accounts
            print("Existing accounts:")

            for acc in accounts:
                print(f"- {acc}")
            account_name = input("Please insert the name of your account: ")

            # Validate that the provided account exists and load it if found
            if Account.findAccount(account_name):
                return account_name,Account(account_name)
            
            else:
                print(f"Account named \"{account_name}\" doesn't exist\n") 