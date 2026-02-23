# Q10 - Simple ATM Simulator

balance = 10000  # starting balance is Rs.10,000

print("Welcome to ATM Simulator")

while True:
    # show the main menu
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a valid number (1-4).")
        continue

    if choice == 1:
        # just show current balance
        print(f"Your current balance is Rs.{balance}")

    elif choice == 2:
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Deposit amount must be greater than 0.")
            else:
                balance += amount
                print(f"Rs.{amount} deposited successfully!")
                print(f"New balance: Rs.{balance}")
        except ValueError:
            print("Invalid amount entered.")

    elif choice == 3:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Withdrawal amount must be greater than 0.")
            # check if minimum balance of Rs.500 will be maintained
            elif balance - amount < 500:
                print("Insufficient balance! Minimum balance of Rs.500 must remain.")
            else:
                balance -= amount
                print("Withdrawal successful!")
                print(f"New balance: Rs.{balance}")
        except ValueError:
            print("Invalid amount entered.")

    elif choice == 4:
        print("Thank you for using ATM. Goodbye!")
        break

    else:
        print("Invalid choice! Please select between 1 and 4.")