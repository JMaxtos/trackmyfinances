import os
from account import Account
from transaction import Transaction
from utils import Utils

# Main menu system for the Track My Finances terminal application
class Menu:
 
    
    # Initialize the menu and load or create user accounts
    def __init__(self):
        
        # Check if the accounts directory is created
        if not os.path.exists(Account.ACCOUNT_DIR):
            os.makedirs(Account.ACCOUNT_DIR
                        )
        # Retrieve all existing accounts (csv files in the current directory)
        accounts = [f[:-4] for f in os.listdir(Account.ACCOUNT_DIR) if f.endswith('.csv')]  
        
        if not accounts:
            print("No accounts found. You must create a new account first.\n")
            # Prompt the user to create an initial account
            self.firstAccount()
        else:
            # Allow user to select and log in to an existing account
             self.loginAccount(accounts)
        
        # Launch the main menu
        self.principalMenu()   


    # Create the first account when none exists
    def firstAccount(self):
                account_name = input("Please insert the name of the new account: ")    
                balance = input ("Please insert initial balance: ")

                # Create and store the first account
                account = Account(account_name,balance)
                self.account = account
                self.account_name = account_name


    # Allow user to log in to an existing account
    def loginAccount(self,accounts):
        while True:
            # Display the current available accounts
            print("Existing accounts:")

            for acc in accounts:
                print(f"- {acc}")
            account_name = input("Please insert the name of your account: ")

            # Validate that the provided account exists and load it if found
            if Account.findAccount(account_name):
                self.account_name = account_name
                self.account = Account(account_name)
                break
            else:
                print(f"Account named \"{account_name}\" doesn't exist\n") 

    # Display the main application menu
    def principalMenu(self,):
            
            # Clear the terminal for better readibility
            Utils.clearTerminal()
            
            print(f'Welcome {self.account_name} to Track My Finances !\n')
            print("1. Accounts Menu")
            print("2. Transactions Menu")
            print("3. Exit Program")

            # Get user input for menu
            choice = Utils.getIntInput('Enter your choice: ', 1, 3)

            # Validate the user input choice
            self.principalMenuChoice(choice)


    # Handle user input from the main menu
    def principalMenuChoice(self,choice):
        # Option 1: Go to accounts menu
        if choice == 1:
            self.accountsMenu()    

        # Option 2: Go to transactions menu    
        if choice == 2:
            self.transactionsMenu()

        # Option 3: Exits program
        if choice == 3:
            # Clear terminal before showing options
            Utils.clearTerminal()

            print("Thank you for using TrackMyFinances!")
            # Safely exits the program
            exit(0)


    # Display the account menu     
    def accountsMenu(self):
            
            # Clear terminal before showing options
            Utils.clearTerminal()
            
            print("Accounts menu\n")
            print("1. Create an account")
            print("2. Find an account")
            print("3. Change account")
            print("4. Show Balance")
            print("5. Exit ")

            
            choice = Utils.getIntInput('Enter your choice: ', 1, 5)
            self.accountsMenuChoice(choice)


    # Handle user input from the accounts menu
    def accountsMenuChoice(self,choice):
        # Option 1: Create new Account
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

        # Option 2: Search for an existing account
        if choice == 2:
            name = input('Please insert the name of the account you want to search: ')
            if Account.findAccount(name):
                print(f"Account {name} exists")
            else:
                print(f"Account {name} doesn't exist")
            input("\nPress Enter to return to Accounts Menu...")
            self.accountsMenu()

        # Option 3: Switch to another account
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

        # Option 4: Display current account balance
        if choice == 4:
            print(f"Current balance for {self.account_name}: {self.account.getBalance()}")
            input("\nPress Enter to return to Accounts Menu...")
            self.accountsMenu()

        # Option 5: Return to the main menu
        if choice == 5:
            self.principalMenu()


    
    # Display the transactions Menu
    def transactionsMenu(self):
            # Clears the Terminal
            Utils.clearTerminal()
            
            # Initialize a transaction manager for the current account
            tx = Transaction(self.account)
            self.transaction = tx
          
            print("Transaction Menu \n")
            print('1. Add an transaction')
            print('2. List all transactions')
            print('3. Show total transactions')
            print('4. Filter transactions ')
            print('5. Exit')       
          

            choice = Utils.getIntInput('Enter your choice: ', 1, 5)
            self.transactionsMenuChoice(choice)

    # Handle user input from the transaction menu
    def transactionsMenuChoice(self,choice):
        # 1. Add an transaction
        if choice == 1:
            self.transaction.addTransaction(100, type='Income', category='Salary')   
            input("\nPress Enter to return to transactions Menu...")
            self.transactionsMenu()
        # 2. List all transactions
        if choice ==2 :
            alltransactions= self.transaction.listAllTransactions()
            self.transaction.printListTransactions(alltransactions)
            input("\nPress Enter to return to transactions Menu...")
            self.transactionsMenu()
        # 3. Show total transactions (TBD)
        # 4. Filter transactions by Category (TBD)
        if choice == 4:
            categoryTransactions = self.transaction.transactionsByFilter(lambda tx : tx['Category']=="Salary") 
            self.transaction.printListTransactions(categoryTransactions)
            input("\nPress Enter to return to transactions Menu...")
            self.transactionsMenu()
        # 6. Exit
        if choice == 6:
             self.principalMenu()

if __name__ == "__main__":
    Menu()