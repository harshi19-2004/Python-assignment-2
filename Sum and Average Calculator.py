# Q13 - Sum and Average Calculator

try:
    count = int(input("How many numbers? "))

    if count <= 0:
        print("Please enter at least 1 number.")
    else:
        numbers = []

        # take numbers from user one by one using a loop
        for i in range(1, count + 1):
            num = float(input(f"Enter number {i}: "))
            numbers.append(num)

        # calculate sum, average, max and min
        total = sum(numbers)
        average = total / count
        maximum = max(numbers)
        minimum = min(numbers)

        print(f"\nSum     : {total}")
        print(f"Average : {average}")
        print(f"Maximum : {maximum}")
        print(f"Minimum : {minimum}")

except ValueError:
    print("Invalid input! Please enter numbers only.")