# Q15 - Prime Number Checker

# function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False   # 0, 1 and negatives are not prime
    if n == 2:
        return True    # 2 is the only even prime
    if n % 2 == 0:
        return False   # all other even numbers are not prime

    # check divisibility from 3 up to square root of n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


# --- Part 1: Check a single number (5 marks) ---
try:
    num = int(input("Enter a number: "))

    if num < 0:
        print(f"{num} is a negative number. Prime check not applicable.")
    elif is_prime(num):
        print(f"{num} is a PRIME number")
    else:
        print(f"{num} is NOT a prime number")

except ValueError:
    print("Invalid input! Please enter a whole number.")


# --- Part 2: Find all primes in a range (2 marks) ---
print()
try:
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))

    if start > end:
        print("Start range should be less than or equal to end range.")
    else:
        prime_list = []

        # go through each number in the range and check if prime
        for n in range(start, end + 1):
            if is_prime(n):
                prime_list.append(n)

        if prime_list:
            print(f"Prime numbers: {', '.join(map(str, prime_list))}")
        else:
            print("No prime numbers found in this range.")

except ValueError:
    print("Invalid input! Please enter whole numbers only.")