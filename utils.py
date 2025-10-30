class Utils:
    # Clear Tearminal for better readibility and better visualization of the terminal app
    @staticmethod
    def clearTerminal():
        import os
        os.system('cls' if os.name == 'nt' else 'clear')


    #  Safely gets an integer input from the user. Repeats until a valid integer within the allowed range is entered.
        
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
