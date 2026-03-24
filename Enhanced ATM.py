# Q10 Bonus - ATM with transaction history

balance = 10000
history = []

while True:

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show History")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance: Rs." + str(balance))

    elif choice == "2":
        try:
            amt = float(input("Enter deposit amount: "))
            if amt <= 0:
                print("Amount should be more than 0")
            else:
                balance = balance + amt
                history.append("Deposited Rs." + str(amt) + " | Balance: Rs." + str(balance))
                print("Deposited! New balance: Rs." + str(balance))
        except:
            print("Enter a valid number")

    elif choice == "3":
        try:
            amt = float(input("Enter withdraw amount: "))
            if amt <= 0:
                print("Amount should be more than 0")
            elif balance - amt < 500:
                print("Cannot withdraw. Min balance Rs.500 must stay.")
            else:
                balance = balance - amt
                history.append("Withdrew Rs." + str(amt) + " | Balance: Rs." + str(balance))
                print("Done! New balance: Rs." + str(balance))
        except:
            print("Enter a valid number")

    elif choice == "4":
        if len(history) == 0:
            print("No transactions done yet")
        else:
            print("\n-- Transaction History --")
            for i in range(len(history)):
                print(str(i+1) + ". " + history[i])

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Wrong choice, try again")