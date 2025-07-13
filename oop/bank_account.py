class BankAccount:
    def __init__(self):
        self.account_holder = ""
        self.address = ""
        self.__pin = ""
        self.__balance = 0
    
    def create_account(self):
        self.account_holder = input("Enter your full name: ")
        self.address = Address()
        while True:
            self.__pin = input("Enter new PIN: ").strip()
            if self.__pin.isdigit() and len(self.__pin) >= 4:
                print("\nPIN setup is successful!")
                break
            else:
                print("\nInvalid PIN!\n1. Minimum length is 4\n2. Only use 0-9 as PIN")
        
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
                print(f"\nDeposit successful! Your new balance is {self.__balance}")
            else:
                print("Invalid amount! Please enter only numbers!")
    
    def withdraw(self):
        if self.check_pin():
            amount_str = input("Enter withdraw amount: ").strip()
            if amount_str.isdigit():
                amount = int(amount_str)
                if amount <= self.__balance():
                    self.__balance -= amount
                    print(f"\nWithdraw successful! Your new balance is {self.__balance}")
                else:
                    print("Insufficient balance!")
            else:
                print("Invalid amount! Please enter only numbers!")
    
    def display_balance(self):
        if self.check_pin():
            print(f"Your balance is {self.__balance}")



class Address:
    def __init__(self):
        pass