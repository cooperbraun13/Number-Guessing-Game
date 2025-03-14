import random
import time

def number_guessing_game():
    """
    A simple number guessing game that demonstrates Python fundamentals
    """
    print("*****Number Guessing Game*****")
    print("Im thinking of a number between 1 and 100.")

    # Variables and random number generation
    random_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    guesses = []
    start_time = time.time()
    
    # Select difficulty
    print("\nSelect your difficulty")
    print("1. Easy (unlimited attempts)")
    print("2. Medium (10 attempts)")
    print("3. Hard (5 attempts)")

    # Handle user input with exception handling
    while True:
        try:
            difficulty = int(input("\nEnter your choice (1-3): "))
            if 1 <= difficulty <= 3:
                break
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")

    # Setting difficulty
    if difficulty == 1:
        max_attempts = float("inf")
        print("\nEasy mode selected, you have unlimited attempts")
    elif difficulty == 2:
        max_attempts = 10
        print(f"\nMedium mode selection, you have {max_attempts} attempts")
    else:
        # Max attempts already set to 5
        print(f"\nHard mode selected, you have {max_attempts} attempts")

    # Main game loop
    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess 1-100: "))
            # Input validation
            if not 1 <= guess <= 100:
                print("Enter a number between 1 and 100.")
                continue

            guesses.append(guess)
            attempts += 1

            # Game logic
            if guess < random_number:
                print("Too low!")
            elif guess > random_number:
                print("Too high!")
            else:
                # Correct guess
                break

            # Display remaining attempts
            if max_attempts != float("inf"):
                attempts_left = max_attempts - attempts
                print(f"Remaining attempts: {attempts_left}")
        
        except ValueError:
            print("Please enter a valid number.")

    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)

    if guess == random_number:
        print(f"\nCongratulations! You guessed the number {random_number} in {attempts} attempts")
        print(f"It took you {elapsed_time} seconds")

        # String formatting and list operations
        print("\nYour guesses: ", end="")
        print(", ".join(str(g) for g in guesses))

        # Calculate and dispalay statistics
        if attempts > 1:
            average_distance = sum(abs(g - random_number) for g in guesses[:-1]) / (attempts - 1)
            print(f"Average distance from target (excluding final guess): {average_distance:.2f}")
    else:
        print(f"Game over! You've used all {max_attempts} attempts")
        print(f"The number was {random_number} ")

    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if play_again.startswith("y"):
        number_guessing_game()
    else:
        print("Thanks for playing!")

# Execute the game
if __name__ == "__main__":
    number_guessing_game()