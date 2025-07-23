# guess a number game, keep track of attempts, and give hints, loop in if player wants to play again
import random
def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    while True:
        number_to_guess = random.randint(1, 100)
        attempts = 0
        guessed_correctly = False

        while not guessed_correctly:
            try:
                guess = int(input("Guess a number between 1 and 100: "))
                attempts += 1

                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    guessed_correctly = True
                    print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            except ValueError:
                print("Please enter a valid integer.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break
# Call the function to start the game
guess_the_number()

# This code defines a simple number guessing game where the user has to guess a randomly selected number