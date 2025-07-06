def km_to_mile(unit):
    return round(unit * 0.621371, 2)

def celsius_to_fahrenheit(unit):
    return round((unit * 9 / 5) + 32, 1)

def kg_to_lb(unit):
    return round(unit * 2.20462, 2)

def unit_converter():
    print('''
        Welcome to Unit Converter! 🚀
        
        Select your preferred conversion!
        1. Kilometer to Mile
        2. Celsius to Fahrenheit
        3. Kilogram to Pound
        4. Exit
    ''')
    while True:
        try:          
            choice = input("Enter your choice: ").strip()

            if choice == "4":
                print("Thanks for using the converter! 👋")
                break
            elif choice not in ["1", "2", "3"]:
                print("Invalid input! Please enter 1-4!")
                continue

            unit = float(input("Enter the value you want to covert: "))

            if choice == "1":
                result = km_to_mile(unit)
                old_unit = "Km"
                new_unit = "Miles"
            elif choice == "2":
                result = celsius_to_fahrenheit(unit)
                old_unit = "°C"
                new_unit = "°F"
            elif choice == "3":
                result = kg_to_lb(unit)
                old_unit = "Kg"
                new_unit = "lbs"
            
            print(f"\n✅ {unit} {old_unit} = {result} {new_unit}")
        
        except ValueError:
            print("Invalid Input! Please enter valid number!")
        except Exception as e:
            print(f"Error: {e}")


unit_converter()