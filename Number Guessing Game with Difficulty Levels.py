# Q16 Bonus - Number Guessing Game with Difficulty Levels

import random

best_score = None

while True:

    print("\nSelect Difficulty:")
    print("1. Easy   (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard   (1 - 1000)")
    print("4. Exit")

    level = input("Enter choice: ")

    if level == "4":
        print("Goodbye!")
        break

    if level == "1":
        low = 1
        high = 50
        attempts = 7
    elif level == "2":
        low = 1
        high = 100
        attempts = 7
    elif level == "3":
        low = 1
        high = 1000
        attempts = 10
    else:
        print("Wrong choice, pick 1 to 4")
        continue

    number = random.randint(low, high)
    print("\nI picked a number between " + str(low) + " and " + str(high))
    print("You have " + str(attempts) + " attempts. Good luck!")

    count = 0
    won = False

    for i in range(1, attempts + 1):
        try:
            guess = int(input("Attempt " + str(i) + ": Enter guess: "))
        except:
            print("Please enter a valid number")
            continue

        count += 1

        if guess == number:
            won = True
            print("Correct! You got it in " + str(count) + " attempt(s)!")
            if best_score == None or count < best_score:
                best_score = count
                print("New best score: " + str(best_score))
            else:
                print("Best score so far: " + str(best_score))
            break
        elif guess < number:
            print("Too low! Attempts left: " + str(attempts - i))
        else:
            print("Too high! Attempts left: " + str(attempts - i))

    if won == False:
        print("Out of attempts! The number was " + str(number))

    again = input("\nPlay again? (yes/no): ")
    if again != "yes":
        print("Thanks for playing!")
        break