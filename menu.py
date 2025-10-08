import os
from account import Account
from transaction import Transaction
class Menu:

    def __init__(self):
        accounts = [f[:-4] for f in os.listdir() if f.endswith('.csv')]  #list of all accounts

        if not accounts:
            print("No accounts found. You must create a new account first.\n")
            self.firstAccount()
        else:
             self.loginAccount(accounts)
        self.principalMenu()   



    def firstAccount(self):
                account_name = input("Please insert the name of the new account: ")    
                balance = input ("Please insert initial balance: ")
                account = Account(account_name,balance)
                self.account = account
                self.account_name = account_name

    def loginAccount(self,accounts):
        while True:
            print("\nExisting accounts:")
            for acc in accounts:
                print(f"- {acc}")
            account_name = input("Please insert the name of your account: ")
            if Account.findAccount(account_name):
                self.account_name = account_name
                self.account = Account(account_name)
                break
            else:
                print(f"Account named \"{account_name}\" doesn't exist\n") 

    def principalMenu(self,):
            print('\n*********************\n')
            print(f'\nWelcome {self.account_name} to Track My Finances !\n')
            print("1. Accounts Menu")
            print("2. Transactions Menu")
            print("3. Exit Program")
            print('\n*********************\n')
            choice = int(input('Enter your choice: '))
            self.principalMenuChoice(choice)



    def principalMenuChoice(self,choice):
        if choice < 1 or choice > 3:
            print("\nInvalid input. Try Again!\n")
            self.principalMenu()
        
        if choice == 1:
            self.accountsMenu()        
        if choice == 2:
            self.transactionsMenu()
        if choice == 3:
            print("Thank you for using TrackMyFinances!")
            exit(0)



    def accountsMenu(self):
            print('\n*********************\n')            
            print("\nAccounts menu\n")
            print("1. Create an account")
            print("2. Find an account")
            print("3. Change account")
            print("4. Show Balance")
            print("5. Exit ")
            print('\n*********************\n')

            choice = int(input('Enter your choice: '))
            self.accountsMenuChoice(choice)



    def accountsMenuChoice(self,choice):
        if choice < 1 or choice > 5:
            print("\nInvalid input. Try Again!\n")
            self.accountsMenu()

        if choice == 1:
            while True:
                user = input("Please insert the name of the new account ")
                if Account.findAccount(user):
                    print(f'Account name {user} is already in use. Please choose another name.\n')
                else:
                    break 

            balance = int(input("Account Initial Balance: "))
            try: 
                Account(user, balance)
                print("Account Created Successfully")
            except:
                raise Exception("Account couldn't be created")
            input("\nPress Enter to return to Accounts Menu...")
            self.accountsMenu()  

        if choice == 2:
            name = input('Please insert the name of the account you want to search: ')
            if Account.findAccount(name):
                print(f"Account {name} exists")
            else:
                print(f"Account {name} doesn't exist")
            input("\nPress Enter to return to Accounts Menu...")
            self.accountsMenu()

        if choice == 3:
            while True:
                new_account = input("Introduce the name of the account you want to access: ")
                if Account.findAccount(new_account):
                    self.account_name = new_account
                    self.account = Account(new_account)
                    break
                else:
                    print(f"Account named \"{new_account}\" doesn't exist\n")
            self.principalMenu()

        if choice == 4:
            print(f"Current balance for {self.account_name}: {self.account.getBalance()}")
            input("\nPress Enter to return to Accounts Menu...")
            self.accountsMenu()

        if choice == 5:
            self.principalMenu()


    
    
    def transactionsMenu(self):
            tx = Transaction(self.account)
            self.transaction = tx
            print('\n*********************\n')
            print("\n Transaction Menu \n")
            print('1. Add an transaction')
            print('2. List all transactions')
            print('3. Show total transactions')
            print('4. Filter transactions by category')
            print('5. Filter transactions by type ')
            print('6. Exit')       
            print('\n*********************\n')

            choice = int(input('Enter your choice: '))
            self.transactionsMenuChoice(choice)

    def transactionsMenuChoice(self,choice):
        if choice == 1:
            self.transaction.addTransaction(100, type='Income', category='Salary')   
            input("\nPress Enter to return to transactions Menu...")
            self.transactionsMenu()
        if choice == 6:
             self.principalMenu()

if __name__ == "__main__":
    Menu()