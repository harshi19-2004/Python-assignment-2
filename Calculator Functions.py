# Q18 - Calculator Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # handle division by zero
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Cannot do modulus by zero!"
    return a % b

def power(a, b):
    return a ** b

def calculator():
    while True:
        print("\n===== Calculator =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 7:
                print("Goodbye!")
                break

            if choice < 1 or choice > 7:
                print("Invalid choice! Enter between 1 and 7.")
                continue

            # take two numbers as input
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            # call the right function based on user choice
            if choice == 1:
                result = add(a, b)
                print(f"Result: {a} + {b} = {result}")
            elif choice == 2:
                result = subtract(a, b)
                print(f"Result: {a} - {b} = {result}")
            elif choice == 3:
                result = multiply(a, b)
                print(f"Result: {a} x {b} = {result}")
            elif choice == 4:
                result = divide(a, b)
                print(f"Result: {a} / {b} = {result}")
            elif choice == 5:
                result = modulus(a, b)
                print(f"Result: {a} % {b} = {result}")
            elif choice == 6:
                result = power(a, b)
                print(f"Result: {a} ^ {b} = {result}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

# run the calculator
calculator()