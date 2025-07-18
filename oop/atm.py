class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()
    
    def menu(self):
        while True:
            try:
                print('''
                                Welcome to ATM!
                                How do you want to proceed?
                                1. Enter 1 to set PIN
                                2. Enter 2 to deposit money
                                3. Enter 3 to withdraw cash
                                4. Enter 4 to check balance
                                5. Enter 5 to change PIN
                                6. Enter 6 to exit
                ''')
                user_input = input("Enter your choice: ").strip()
                if user_input == '6':
                    print("\nThank you for using ATM!🙏")
                    break
                if user_input not in ['1', '2', '3', '4', '5']:
                    print("\n⚠️ Invalid input! Please enter 1-6!")
                    continue

                if user_input == "1":
                    self.create_pin()
                elif user_input == "2":
                    self.deposit()
                elif user_input == "3":
                    self.withdraw()
                elif user_input == "4":
                    self.check_balance()
                elif user_input == "5":
                    self.change_pin()
            
            except ValueError:
                print("\nInvalid input! Please enter a valid number!")
            except Exception as e:
                print(f"Error: {e}")
    
    def create_pin(self):
        if self.pin == "":
            while True:
                self.pin = input("Enter a PIN: ").strip()
                if self.pin.isdigit() and len(self.pin) >= 4:   
                    print("\n✅ PIN setup is successful! 🚫 Don't share it with anyone!")
                    break
                else:
                    print("\n⚠️  Invalid PIN!\n1. Minimum PIN length is 4 digits\n2. Only digits can be used as PIN")
        else:
            print("\n⚠️  A PIN is already created!")
    
    def check_pin(self):
        if self.pin != "":
            attempt = 3
            while attempt > 0:
                try:
                    inputted_pin = input("\nEnter your PIN: ").strip()
                    if inputted_pin == self.pin:
                        return True
                    else:
                        attempt -= 1
                        if attempt == 0:
                            print("⛔ Contact administration to reset your PIN! ⛔")
                        else:
                            print("\n❌ Wrong PIN! Try again!")
                            print(f"{attempt} Left")
                except ValueError:
                    print("\nInvalid PIN! Please enter valid PIN!")
        else:
            print("⚠️  PIN is not set yet! Set PIN first!")
    
    def deposit(self):
        temp = self.check_pin()
        if temp:
            amount_str = input("\nEnter deposit amount: ")
            if amount_str.isdigit():
                amount = int(amount_str)
                self.balance += amount
                print(f"\n✅ Deposit successful! Your new balance is ${self.balance}")
            else:
                print("\n⚠️  Invalid amount! Please enter numbers only!")
    
    def withdraw(self):
        temp = self.check_pin()
        if temp:
            amount_str = input("\nEnter withdraw amount: ")
            if amount_str.isdigit():
                amount = int(amount_str)
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"\n✅ Cash withdrawal successful! Your new balance is ${self.balance}")
                else:
                    print("\n⚠️  Insufficient balance!")
            else:
                print("\n⚠️  Invalid amount! Please enter numbers only!")
    def check_balance(self):
        temp = self.check_pin()
        if temp:
            print(f"\nYour balance is ${self.balance}")
    
    def change_pin(self):
        temp = self.check_pin()
        if temp:
            self.pin = input("\nEnter your new PIN: ")
            print("\n✅ New PIN setup is successful! 🚫 Don't share it with anyone!")


my_atm = Atm()
my_atm.menu()
