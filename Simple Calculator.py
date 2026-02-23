# Simple calculator program

# taking numbers from user
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except:
    print("Please enter valid numbers.")
    exit()

print("\nResults:")

# addition
print(num1, "+", num2, "=", num1 + num2)

# subtraction
print(num1, "-", num2, "=", num1 - num2)

# multiplication
print(num1, "*", num2, "=", num1 * num2)

# division
if num2 != 0:
    print(num1, "/", num2, "=", round(num1 / num2, 2))
else:
    print("Division not possible (cannot divide by zero)")

# modulus
if num2 != 0:
    print(num1, "%", num2, "=", num1 % num2)
else:
    print("Modulus not possible (cannot divide by zero)")

# exponent
print(num1, "^", num2, "=", num1 ** num2)