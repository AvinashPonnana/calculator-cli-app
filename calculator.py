# 1. Operation Functions

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers (handles divide-by-zero)."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b



# 2. Display Menu

def show_menu():
    """Display available operations."""
    print("\n===== CLI Calculator =====")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("===========================")



# 3. Main Calculator Loop

def calculator():
    """Main function to run the calculator app."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting... Goodbye!")
            break

        # Check if user entered a valid choice
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue

        # Take numeric inputs
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        # Perform calculation based on choice
        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operation = '/'

        print(f" Result: {num1} {operation} {num2} = {result}")



# 4. Entry Point

if __name__ == "__main__":
    calculator()
