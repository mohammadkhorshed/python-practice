class BankAccount:
    def __init__(self):
        self.account_holder = ""
        self.address = ""
        self.pin = ""
        self.balance = 0
    
    def create_account(self):
        self.account_holder = input("Enter your full name: ")
        self.address = Address()
        while True:
            self.pin = input("Enter new PIN: ").strip()
            if self.pin.isdigit() and len(self.pin) >= 4:
                print("\nPIN setup is successful!")
                break
            else:
                print("\nInvalid PIN!\n1. Minimum length is 4\n2. Only use 0-9 as PIN")
        
    def check_pin(self):
        if self.pin:
            attempt = 3
            while attempt > 0:
                try:
                    input_pin = input("Enter your PIN: ").strip()
                    if input_pin == self.pin:
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


class Address:
    def __init__(self):
        pass