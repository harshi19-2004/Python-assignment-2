# Q14 - Factorial Calculator

try:
    num = int(input("Enter a number: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")

    elif num == 0:
        print("0! = 1")

    else:
        factorial = 1
        steps = []  # store each step for display

        # calculate factorial using a loop
        for i in range(num, 0, -1):
            factorial *= i
            steps.append(str(i))

        # join steps with x to show working
        step_str = " x ".join(steps)
        print(f"{num}! = {step_str} = {factorial}")

except ValueError:
    print("Invalid input! Please enter a whole number.")