import csv
import os
class Account :
    def __init__(self,account_name):
        self.account_name = account_name
        self.createCSVFile()
    
    def createCSVFile(self):
        file =f"{self.account_name}.csv"
        
        if os.path.isfile(file):
            print(f'Account name {file} is already in use ')

        with open(file,mode='w',newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Action', 'Category' , 'Value'])

if __name__ == "__main__":
    user = input("Account name: ")
    ac1 = Account(user)
      
