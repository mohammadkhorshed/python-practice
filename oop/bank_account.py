class BankAccount:
    def __init__(self):
        self.account_holder = ""
        self.address = ""
        self.__pin = ""
        self.__balance = 0
        self.transactions = []
    
    def create_account(self):
        self.account_holder = input("Enter your full name: ")
        self.address = Address()
        while True:
                input_pin = input("Enter new PIN: ").strip()
                if input_pin.isdigit() and len(input_pin) >= 4:
                    self.__pin = input_pin
                    print("PIN setup is successful!")
                    break
                else:
                    print("\nInvalid PIN!\n1. Minimum length is 4\n2. Only use 0-9 as PIN")
        print("\nAccount successfully created!")
        print(f"\nName: {self.account_holder}")
        self.address.print_address()
        
    def check_pin(self):
        if self.__pin:
            attempt = 3
            while attempt > 0:
                try:
                    input_pin = input("Enter your PIN: ").strip()
                    if input_pin == self.__pin:
                        return True
                    else:
                        attempt -= 1
                        if attempt == 0:
                            print("Please contact administration to reset your PIN!")
                        else:
                            print("\nWrong PIN! Try again!")
                            print(f"\nAttempt left: {attempt}")
                except ValueError:
                    print("Invalid input! Please input valid PIN!")
        else:
            print("PIN is not set! Create a account first!")
    
    def deposit(self):
        if self.check_pin():
            amount_str = input("Enter deposit amount: ").strip()
            if amount_str.isdigit():
                amount = int(amount_str)
                self.__balance += amount
                self.transactions.append(f"Deposit: {amount}")
                print(f"\nDeposit successful! Your new balance is {self.__balance}")
            else:
                print("Invalid amount! Please enter only numbers!")
    
    def withdraw(self):
        if self.check_pin():
            amount_str = input("Enter withdraw amount: ").strip()
            if amount_str.isdigit():
                amount = int(amount_str)
                if amount <= self.__balance:
                    self.__balance -= amount
                    self.transactions.append(f"Withdraw: {amount}")
                    print(f"\nWithdraw successful! Your new balance is {self.__balance}")
                else:
                    print("Insufficient balance!")
            else:
                print("Invalid amount! Please enter only numbers!")
    
    def display_balance(self):
        if self.check_pin():
            print(f"Your balance is {self.__balance}")
    
    def change_pin(self):
        if self.check_pin():
            while True:
                input_pin = input("Enter new PIN: ").strip()
                if input_pin.isdigit() and len(input_pin) >= 4:
                    self.__pin = input_pin
                    print("\nPIN setup is successful!")
                    break
                else:
                    print("\nInvalid PIN!\n1. Minimum length is 4\n2. Only use 0-9 as PIN")

    def change_address(self):
        if self.check_pin():
            self.address.add_address()
    
    def show_transactions(self):
        if self.transactions:
            print("Transaction history: ")
            for idx, item in enumerate(self.transactions):
                print(f"{idx + 1}. {item}")
        else:
            print("There is not transaction history!")
            




class Address:
    def __init__(self):
        self.postal_code = ""
        self.city = ""
        self.division = ""
        self.add_address()
    
    def __str__(self):
        return f"Postal code: {self.postal_code}\nCity: {self.city}\nDivision: {self.division}"
    
    def add_address(self):
        while True:
            input_postal_code = input("Enter your postal code: ")
            if input_postal_code.isdigit():
                self.postal_code = input_postal_code
                break
            else:
                print("\nInvalid postal code! Use only numbers!")
        self.city = input("Enter your city name: ")
        self.division = input("Enter your division name: ")
    
    def print_address(self):
        print(f"Postal code: {self.postal_code}")
        print(f"City: {self.city}")
        print(f"Division: {self.division}")
    
