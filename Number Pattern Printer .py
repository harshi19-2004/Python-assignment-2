# Q11 - Number Pattern Printer

try:
    print("Select a pattern:")
    print("1. Increasing row (1 / 1 2 / 1 2 3...)")
    print("2. Repeated number (1 / 2 2 / 3 3 3...)")
    print("3. Reverse triangle (5 4 3 2 1 / 4 3 2 1...)")
    print("4. Pyramid pattern (1 / 1 2 1 / 1 2 3 2 1...)")

    pattern = int(input("Enter pattern choice (1-4): "))
    height = int(input("Enter height: "))

    if height <= 0:
        print("Height must be greater than 0.")

    elif pattern == 1:
        # each row prints numbers from 1 to row number
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    elif pattern == 2:
        # each row repeats the row number i times
        for i in range(1, height + 1):
            for j in range(i):
                print(i, end=" ")
            print()

    elif pattern == 3:
        # starts from height down to 1, decreasing each row
        for i in range(height, 0, -1):
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()

    elif pattern == 4:
        # pyramid: go up to i then back down
        for i in range(1, height + 1):
            # ascending part
            for j in range(1, i + 1):
                print(j, end="")
            # descending part (skip the peak)
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()

    else:
        print("Invalid pattern choice! Please enter between 1 and 4.")

except ValueError:
    print("Invalid input! Please enter numbers only.")