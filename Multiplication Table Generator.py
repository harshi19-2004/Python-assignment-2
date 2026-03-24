# Q12 - Multiplication Table Generator

try:
    number = int(input("Enter number: "))
    end_range = int(input("Enter range (end): "))

    if end_range <= 0:
        print("Range must be greater than 0.")
    else:
        # print multiplication table for the given number
        print(f"\nMultiplication Table of {number}")
        for i in range(1, end_range + 1):
            print(f"{number} x {i} = {number * i}")

    # bonus - full 1 to 10 grid
    print("\n--- Bonus: Full Multiplication Table (1-10) ---\n")

    # print top header row
    print("    ", end="")
    for i in range(1, 11):
        print(f"{i:4}", end="")
    print()

    # print separator line
    print("  " + "-" * 42)

    # print each row with row label
    for i in range(1, 11):
        print(f"{i:2} |", end="")
        for j in range(1, 11):
            print(f"{i * j:4}", end="")
        print()

except ValueError:
    print("Invalid input! Please enter numbers only.")