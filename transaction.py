import os
import csv
from datetime import datetime

class NullValue(Exception):
    pass
class Transaction:
    def __init__(self, account):
        self.account = account 

    def addTransaction(self, amount, type='Income', category='General'):
        #Add a transaction and updates the balance on the CSV file
        amount = float(amount)
        if type.lower() == 'expense':
            self.account.balance -= amount
        else:
            self.account.balance += amount

        
        #Reads all CSV
        with open(self.account.file, 'r', newline='', encoding='utf-8') as f:
            lines = list(csv.reader(f))

        # Updates the balance
        lines[0][1] = str(self.account.balance)

        # Adds new Transaction
        lines.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), type, category, str(amount)])

        # Writes Everything on the CSV
        with open(self.account.file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(lines)
    
  
            
