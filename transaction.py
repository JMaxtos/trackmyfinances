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

        # Read all CSV data
        with open(self.account.file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            lines = list(reader)

        # Skip header and find last balance
        if len(lines) > 1:
            # Get current total balance
            last_balance = float(lines[-1][-1])  
        else:
            last_balance = 0

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

        # Write all lines back to CSV
        with open(self.account.file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(lines)

        # Update balance in memory
        self.account.balance = new_balance

        print(f"\n Transaction added successfully! New balance: {new_balance:.2f}")
    
  
            
