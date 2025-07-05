def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def power(x, y):
    return x ** y

def root(x, y):
    if y == 0:
        return "Error: Cannot use 0 as root index!"
    if x < 0 and y % 2 == 0:
        return "Error: Cannot take even root of negative number!"
    try:
        return x ** (1 / y)
    except:
        return "Error: Invalid root calculation!"
    
def percentage(x, y):
    return x * (y / 100)


def calculator():
    print("Simple Calculator 🔣")
    print("Select operation:")
    print("1. Add(+)")
    print("2. Subtract(-)")
    print("3. Multiply(×)")
    print("4. Divide(÷)")
    print("5. Power(a**b)")
    print("6. Root(y√x)")
    print("7. Percentage(%)")
    print("8. Exit")

    while True:
        try:
            choice = input("Enter your choice (1-8):")

            if choice == "8":
                print("Thanks for using the calculator! 👋")
                break

            if choice not in ['1', '2', '3', '4', '5', '6', '7']:
                print("Invalid input! Please enter 1-8!")
                continue

            num1 = float(input("Please enter first number: "))
            num2 = float(input("Please enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                operation = "+"          
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            elif choice == '5':
                result = power(num1, num2)
                operation = "**"
            elif choice == '6':
                result = root(num1, num2)
                operation = "√"
            elif choice == '7':
                result = percentage(num1, num2)
                operation = "%"

            if isinstance(result, str):
                print(f"Result: {result}")
            else:
                print(f"Result: {num1} {operation} {num2} = {result}")
            
        except ValueError:
            print("Invalid input! Please enter valid number!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()