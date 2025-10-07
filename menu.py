class Menu:
    def __init__(self):
        self.principalMenu()
            
    def principalMenu(self):
        while True:
            print(f'\n Welcome {self.account_name} to Track My Finances !')
            print("1. Create an account")
            print("2. Find an account ")
            print("3. Add a transaction")

    def transactionsMenu(self):
        while True:
            print("\n*****Transaction Menu*****")
            print('1. Add an transaction')
            print('2. List all transactions')
            print('3. Show total transactions')
            print('4. Filter transactions by category')
            print('5. Filter transactions by type ')
            print('6. Exit')       