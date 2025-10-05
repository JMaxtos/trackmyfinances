import csv
import os
class Account :
    def __init__(self,account_name,balance = 0):
        self.account_name = account_name
        self.balance = balance
        self.createCSVFile()
    
    def getBalance(self):
        return self.balance
    
    def updateBalance(self,amount):
        try:
            amount = int(amount)  
        except ValueError:
            raise TypeError("Only integers are allowed as amount")
        self.balance += amount
        
    def createCSVFile(self):
        file =f"{self.account_name}.csv"
        
        if os.path.isfile(file):
            print(f'Account name {file} is already in use ')

        with open(file,mode='w',newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Type', 'Category' , 'Value'])

if __name__ == "__main__":
    user = input("Account name: ")
    balance =int( input("Account Balance: "))
    ac1 = Account(user,balance)
    print(f'Current balance:  {ac1.getBalance()}')
    amount =int( input("New ammount to total: "))
    ac1.updateBalance(amount)
    print(f'Currentbalance after Update:  {ac1.getBalance()}')
    amount =int( input("New ammount to total: "))
    ac1.updateBalance(amount)  
    print(f'Currentbalance after Update:  {ac1.getBalance()}')