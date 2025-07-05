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
        return "Error: Cannot root by zero!"
    return x ** (1 / y)

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
    print("6. Exit")

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