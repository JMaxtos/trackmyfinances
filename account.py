import csv
import os

# Account class representes a financial account
# with a name, balance, and an associated CSV file
# to store transactions.

class Account :
    def __init__(self,account_name,balance = 0):
        self.account_name = account_name
        self.balance = balance
        self.createCSVFile()
    
    # Returns the current balance of the account
    def getBalance(self):
        return self.balance
    
    # Updates the account balance by adding the given amount
    def updateBalance(self,amount):
        try: #Validate that the input can be converted to float 
            amount = float(amount)  
        except ValueError:
            raise TypeError("Only floats are allowed as amount") 
        self.balance += amount

    # Create the CSV file 
    def createCSVFile(self):
        file =f"{self.account_name}.csv"
        with open(file,mode='w',newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Type', 'Category' , 'Value'])

if __name__ == "__main__":
    while True:
        user = input("Account name: ")
        file = f"{user}.csv"
        if os.path.isfile(file):
            print(f'Account name {file} is already in use. Please choose another name.\n')
        else:
            break  
    balance =int( input("Account Balance: "))
    ac1 = Account(user,balance)
    print(f'Current balance:  {ac1.getBalance()}')
    amount =int( input("New ammount to total: "))
    ac1.updateBalance(amount)
    print(f'Currentbalance after Update:  {ac1.getBalance()}')
    amount =int( input("New ammount to total: "))
    ac1.updateBalance(amount)  
    print(f'Currentbalance after Update:  {ac1.getBalance()}')