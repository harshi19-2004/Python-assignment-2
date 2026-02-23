# Q20 - Number System Functions

def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def fibonacci(n):
    if n <= 0:
        return "Enter a positive number"
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
    return b

def sum_of_digits(n):
    # add up each digit of the number
    n = abs(n)  # handle negative numbers
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

def reverse_number(n):
    # reverse the digits of a number
    is_negative = n < 0
    reversed_str = str(abs(n))[::-1]
    result = int(reversed_str)
    return -result if is_negative else result

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    # sum of each digit raised to the power of total digits
    total = sum(int(d) ** power for d in digits)
    return total == n

def gcd(a, b):
    # euclidean algorithm for greatest common divisor
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # lcm = (a * b) / gcd(a, b)
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def is_perfect_number(n):
    if n <= 1:
        return False
    # sum all divisors except the number itself
    divisor_sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
    return divisor_sum == n

def math_menu():
    while True:
        print("\n===== Math Functions Menu =====")
        print("1.  Factorial")
        print("2.  Is Prime")
        print("3.  Fibonacci")
        print("4.  Sum of Digits")
        print("5.  Reverse Number")
        print("6.  Is Armstrong")
        print("7.  GCD")
        print("8.  LCM")
        print("9.  Is Perfect Number")
        print("10. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 10:
                print("Goodbye!")
                break

            if choice in [1, 2, 3, 4, 5, 6, 9]:
                n = int(input("Enter a number: "))

                if choice == 1:
                    print(f"{n}! = {factorial(n)}")
                elif choice == 2:
                    print(f"{n} is {'PRIME' if is_prime(n) else 'NOT prime'}")
                elif choice == 3:
                    print(f"Fibonacci({n}) = {fibonacci(n)}")
                elif choice == 4:
                    print(f"Sum of digits of {n} = {sum_of_digits(n)}")
                elif choice == 5:
                    print(f"Reversed: {reverse_number(n)}")
                elif choice == 6:
                    print(f"{n} is {'an Armstrong' if is_armstrong(n) else 'NOT an Armstrong'} number")
                elif choice == 9:
                    print(f"{n} is {'a Perfect' if is_perfect_number(n) else 'NOT a Perfect'} number")

            elif choice in [7, 8]:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                if choice == 7:
                    print(f"GCD({a}, {b}) = {gcd(a, b)}")
                elif choice == 8:
                    print(f"LCM({a}, {b}) = {lcm(a, b)}")

            else:
                print("Invalid choice! Enter between 1 and 10.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

# run the menu
math_menu()