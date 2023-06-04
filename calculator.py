def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

print("Calculator App")

while True:
    print("\nOperations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Select an operation (1-5): ")

    if choice == '5':
        print("Exiting the calculator app. Goodbye!")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid choice. Please select a valid operation.")
