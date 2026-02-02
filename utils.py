from datetime import datetime

class Utils:
    # Clear Tearminal for better readibility and better visualization of the terminal app
    @staticmethod
    def clearTerminal():
        import os
        os.system('cls' if os.name == 'nt' else 'clear')


    #  Safely gets an integer input from the user. Repeats until a valid integer within the allowed range is entered
    @staticmethod
    def getIntInput(prompt, min_value=None, max_value=None):
       
        while True:
            user_input = input(prompt)
            if not user_input.isdigit():
                print(" Invalid input. Please enter a number.")
                continue

            value = int(user_input)

            if min_value is not None and value < min_value:
                print(f" Please enter a number >= {min_value}")
                continue

            if max_value is not None and value > max_value:
                print(f" Please enter a number <= {max_value}")
                continue

            return value
        
    # Validates alphabetical strings
    @staticmethod 
    def isValidString(word:str)->bool:
        if not word:
            return False
        return all(c.isalpha() or c.isspace() for c in word)
    
    # Validates month format
    @staticmethod
    def validateMonth(month:int):
        if 1 <= month <= 12:
            return month
        raise ValueError("Invalid month. Must be between 1 and 12.")
        
    # Validates year format
    @staticmethod
    def validateYear(year:int):

        if 1000 <= year <= 9999:
            return year
        raise ValueError("Invalid year. Must be 4 digits.")
    
    @staticmethod
    def parseDate(date_str: str) -> datetime:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def parseOnlyDate(date_str: str):
        return datetime.strptime(date_str, "%Y-%m-%d").date()

