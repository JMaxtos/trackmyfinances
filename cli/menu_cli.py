import os
from classes.account import Account
from classes.transaction import Transaction
from classes.utils import Utils
from datetime import datetime

# Main menu system for the Track My Finances terminal application
class CLIMenu:
    MENU_TITLES = {"main": "Track My Finances","accounts":"Accounts Menu","transactions":"Transactions Menu","filters":"Filters Menu","login":"Welcome to TrackMyFinances!"}
    MAIN_MENU_OPTIONS = ["Accounts Menu","Transactions Menu","Exit Program"]
    TRANSACTIONS_MENU = ["Add an transaction","List all transactions","Transaction Filter Menu", "Exit Menu"]
    ACCOUNTS_MENU = ["Create an account","Find an account","Change account","Show Balance","Exit Menu"]
    FILTERS_MENU = ["Filter by type","Filter by category","Filter by month","Filter by year","Filter by specific date","Exit Menu"]
    LOGIN_MENU  = [ "Create New Account","Login to an existing account","Exit Program"]  

    # Initialize the menu and load or create user accounts
    def __init__(self):
        self.account_name = None
        self.account = None
        # Check if the accounts directory is created
        if not os.path.exists(Account.ACCOUNT_DIR):
            os.makedirs(Account.ACCOUNT_DIR
                        )
        # Retrieve all existing accounts (csv files in the current directory)
        self.accounts = Account.listAllAccounts()
        
        if not self.accounts or self.accounts == None:
            print("No accounts found. You must create a new account first.\n")
            # Prompt the user to create an initial account
            self.account_name, self.account = Account.createAccount()
        else:
            self.loginMenu()
        
        # Launch the main menu
        self.principalMenu()   

    # ====== Login Menu ======  
    def loginMenu(self):
        choice = self.displayMenu(self.MENU_TITLES["login"], self.LOGIN_MENU)
        self.loginMenuChoice(choice)

    def loginMenuChoice(self,choice):
        if choice == 1:
            _, _ = Account.createAccount()
            self.loginMenu()
            
        elif choice == 2:
            self.accounts = Account.listAllAccounts()
            self.account_name, self.account = Account.loginAccount(self.accounts)
        elif choice == 3:
            Utils.clearTerminal()

            print("Thank you for using TrackMyFinances!")
            # Safely exits the program
            exit(0)
    

    # ====== Main Menu ======  
    # Function that displays the menus
    def displayMenu(self, title, options):
        Utils.clearTerminal()

        if self.account_name:
            print(f"Account: {self.account_name}\n")
        print(f"{title}\n")
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")
        return Utils.getIntInput("Choose an option: ", 1, len(options))
    
    # Display the main application menu
    def principalMenu(self,):
           while True:
            # Display main Menu
            choice = self.displayMenu(self.MENU_TITLES["main"], self.MAIN_MENU_OPTIONS)
          
            # Validate the user input choice
            self.principalMenuChoice(choice)


    # Handle user input from the main menu
    def principalMenuChoice(self,choice):
        # accounts menu
        if choice == 1:
            self.accountsMenu()    

        # transactions menu    
        if choice == 2:
            self.transactionsMenu()

        # Exits program
        if choice == 3:
            # Clear terminal before showing options
            Utils.clearTerminal()

            print("Thank you for using TrackMyFinances!")
            # Safely exits the program
            exit(0)


    # ====== Accounts Menu ======  
    # Display the account menu     
    def accountsMenu(self):
        choice = self.displayMenu(self.MENU_TITLES["accounts"], self.ACCOUNTS_MENU)
        self.accountsMenuChoice(choice)

    # Handle user input from the accounts menu
    def accountsMenuChoice(self,choice):
        # Option 1: Create new Account
        if choice == 1:
            _,_ = Account.createAccount()
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
                if new_account == self.account_name:
                    self.accountsMenu()
                elif Account.findAccount(new_account):
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


    
    # ====== Transactions Menu ======  
    # Display menu
    def transactionsMenu(self):
        # Initialize a transaction manager for the current account
        self.transaction = Transaction(self.account)
         
        choice = self.displayMenu(self.MENU_TITLES["transactions"], self.TRANSACTIONS_MENU)
        self.transactionsMenuChoice(choice)

    # Handle user input from the transaction menu
    def transactionsMenuChoice(self,choice):
        # 1 Add a transaction
        if choice == 1:
            while True:
                try:
                    transactionAmount = int(input("Please insert the amount of the Transaction: "))
                    break
                except ValueError:
                     print("Invalid amount. Please insert a number.")

            while True:
                transactionType = int(input("\t1. Income\n\t2. Expense\nPlease insert the Type of the Transaction: "))
                if transactionType in (1, 2):
                    transactionType = Transaction.validateTransactionType(transactionType)
                    break
            
            while True:
                transactionCategory = input("Please insert the Category of the Transaction: ")
                # Verify category name allowing spaces between words
                if Utils.isValidString(transactionCategory):
                    break
            try:
                self.transaction.addTransaction(transactionAmount, type=transactionType, category=transactionCategory)   
            except:
                raise Exception("Transaction couldn't be created. Please Try again")
            input("\nPress Enter to return to transactions Menu...")
            self.transactionsMenu()


        #  List all transactions
        if choice ==2 :
            alltransactions= self.transaction.listAllTransactions()
            self.transaction.printListTransactions(alltransactions)
            input("\nPress Enter to return to transactions Menu...")
            self.transactionsMenu()


        # Transaction Filter Menu
        if choice == 3 :
         self.transactionFilterMenu()

        # Exit
        if choice == 4:
             self.principalMenu()



    # Display Transaction Filter Menu
    def transactionFilterMenu(self):
        choice = self.displayMenu(self.MENU_TITLES["filters"], self.FILTERS_MENU)
        self.transactionFiltersMenuChoice(choice)

    # Handle user input from the filter transaction menu
    def transactionFiltersMenuChoice(self,choice):
        if choice == 1: # type
            while True:
                type = input("Please insert the Type you want to filter: ")
                if Utils.isValidString(type):
                    break
            typeTransactions = self.transaction.transactionsByFilter(lambda tx : tx['Type']== type) 
            self.transaction.printListTransactions(typeTransactions)
            input("\nPress Enter to return to transactions Menu...")
            self.transactionFilterMenu()


        if choice == 2: # category
            while True:
                category = input("Please insert the Category you want to filter: ")
                if Utils.isValidString(category):
                    break
            categoryTransactions = self.transaction.transactionsByFilter(lambda tx : tx['Category']== category) 
            self.transaction.printListTransactions(categoryTransactions)
            input("\nPress Enter to return to transactions Menu...")
            self.transactionFilterMenu()
    
        
        if choice == 3: # month and year
            while True:
                try:
                    year = Utils.validateYear(input("Please insert the year you want to filter: "))
                    month = Utils.validateMonth(int(input("Please insert the month you want to filter: ")))
                    break
                except ValueError as e:
                    print(e) 
            categoryTransactions = self.transaction.transactionsByFilter(lambda tx: (
        (d := Utils.parseDate(tx['Date'])).year == year
        and d.month == month
             ))
            self.transaction.printListTransactions(categoryTransactions)
            input("\nPress Enter to return to transactions Menu...")
            self.transactionFilterMenu()
        
        if choice == 4: # year
            while True:
                try:
                    year = Utils.validateYear(input("Please insert the year you want to filter: "))
                    break
                except ValueError as e:
                    print(e)

            yearTransactions = self.transaction.transactionsByFilter(
            lambda tx: Utils.parseDate(tx["Date"]).year == year
            )
            self.transaction.printListTransactions(yearTransactions)
            input("\nPress Enter to return to transaction filter menu...")
            self.transactionFilterMenu()
        
        if choice == 5:  # Filter by specific date
            while True:
                date_str = input("Please insert the date (YYYY-MM-DD): ")
                try:
                    target_date = Utils.parseOnlyDate(date_str)
                    break
                except ValueError:
                    print("Invalid date format")

            dateTransactions = self.transaction.transactionsByFilter(
            lambda tx: Utils.parseDate(tx['Date']).date() == target_date
            )
            
            self.transaction.printListTransactions(dateTransactions)
            input("\nPress Enter to return...")
            self.transactionFilterMenu()
