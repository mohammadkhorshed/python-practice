class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()
    
    def menu(self):
        while True:
            try:
                user_input = input('''
                                Welcome to ATM!
                                How you want tp proceed?
                                1. Enter 1 to create PIN
                                2. Enter 2 to deposit money
                                3. Enter 3 to withdraw cash
                                4. Enter 4 to check balance
                                5. Enter 5 to change PIN
                                6. Enter 6 to exit
                ''').strip()
                if user_input == '6':
                    print("Thank you for using ATM!🙏")
                    break
                if user_input not in ['1', '2', '3', '4', '5']:
                    print("⚠️ Invalid input! Please enter 1-6!")
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
                print("Invalid input! Please enter a valid number!")
            except Exception as e:
                print(f"Error: {e}")