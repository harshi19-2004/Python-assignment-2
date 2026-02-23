# Q16 - Number Guessing Game

import random

best_score = None  # track best score across games (bonus)

while True:
    # computer picks a random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts_used = 0
    guessed_correct = False

    print("\n=============================")
    print("   Welcome to Guessing Game!")
    print("=============================")
    print(f"I picked a number between 1 and 100. You have {max_attempts} attempts.")

    for attempt in range(1, max_attempts + 1):
        attempts_remaining = max_attempts - attempt

        try:
            guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # check if the guess is within range
        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            continue

        # bonus - give a hint if guess is within 5 of the answer
        difference = abs(guess - secret_number)
        if difference <= 5 and guess != secret_number:
            print("You are very close! (within 5)")

        if guess == secret_number:
            guessed_correct = True
            attempts_used = attempt
            print(f"Correct! You guessed it in {attempts_used} attempt(s). Well done!")

            # update best score if this is better
            if best_score is None or attempts_used < best_score:
                best_score = attempts_used
                print(f"New best score: {best_score} attempt(s)!")
            else:
                print(f"Your best score so far: {best_score} attempt(s).")
            break

        elif guess < secret_number:
            print(f"Too low! Attempts remaining: {attempts_remaining}")
        else:
            print(f"Too high! Attempts remaining: {attempts_remaining}")

    # if user ran out of attempts
    if not guessed_correct:
        print(f"\nBetter luck next time! The number was {secret_number}.")
        if best_score:
            print(f"Your best score so far: {best_score} attempt(s).")

    # ask if user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing. Goodbye!")
        break