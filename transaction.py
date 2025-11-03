import os
import csv
from datetime import datetime

class NullValue(Exception):
    pass
class Transaction:
    def __init__(self, account):
        self.account = account 

    def addTransaction(self, amount, type='Income', category='General'):
        
        # Validate and convert amount
        try:
            amount = float(amount)
        except ValueError:
            raise NullValue("Invalid amount. Please provide a numeric value.")
          
        try:
            # Read all CSV data
            with open(self.account.file, 'r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                lines = list(reader)

            # Skip header and find last balance
            if len(lines) > 1:
                # Get current total balance
                last_balance = float(lines[-1][-1])  
            else:
                last_balance = 0.0
        except (FileNotFoundError,IndexError,ValueError):
                last_balance = 0.0

        # Update balance based on transaction type
        if type == 'Expense':
            new_balance = last_balance - amount
        else:
            new_balance = last_balance + amount

        # Append new transaction line
        new_transaction = [ 
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            type.capitalize(),
            category.capitalize(),
            amount,
            new_balance
        ]
        lines.append(new_transaction)

        # Append the new transaction to the file
        with open(self.account.file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(new_transaction)

        # Update balance in memory
        self.account.balance = new_balance

        print(f"\nTransaction added successfully!\nType: {type.capitalize()} | Category: {category.capitalize()} | Ammount: {amount:.2f}\nNew balance: {new_balance:.2f}")
    
    # Function that list all the  transactions on the account
    def listAllTransactions(self):
        with open(self.account.file,"r",newline="",encoding='utf-8') as f:
            # Reads lines by column names
            reader = csv.DictReader(f)
            return list(reader)
        
    # Function that prints a list of transactions
    def printListTransactions(self,transactions):
        if not transactions:
            print(" No transactions found.")
        else:
            print("\n List of all Transactions")
            for t in transactions:
                print(f"{t['Date']} | {t['Type']} | {t['Category']} | {t['Value']} | {t['Balance']}")

    # Function that lists transactions that match the condition
    def transactionsByFilter(self,condition):
        transactions= self.listAllTransactions()
        return [filteredTransactions for filteredTransactions in transactions if condition(filteredTransactions)]
            
