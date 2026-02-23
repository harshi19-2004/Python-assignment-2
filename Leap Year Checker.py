# Q8 - Leap Year Checker
# This program checks whether a given year is a leap year or not
# based on the rule:
# A year is a leap year if it is divisible by 4 AND
# (not divisible by 100 OR divisible by 400)

try:
    year = int(input("Enter a year: "))

    # Checking if year is positive
    if year <= 0:
        print("Invalid input! Year must be a positive number.")
    else:
        # Applying leap year logic
        if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
            print(f"\n{year} is a Leap Year.")
            
            # Explaining reason
            if year % 400 == 0:
                print("Reason: It is divisible by 400.")
            else:
                print("Reason: It is divisible by 4 and not divisible by 100.")
        else:
            print(f"\n{year} is NOT a Leap Year.")
            
            # Explaining reason
            if year % 4 != 0:
                print("Reason: It is not divisible by 4.")
            elif year % 100 == 0 and year % 400 != 0:
                print("Reason: It is divisible by 100 but not divisible by 400.")

except ValueError:
    print("Invalid input! Please enter a valid integer year.")
except Exception as e:
    print("Something went wrong:", e)