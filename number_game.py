import time
import random

def number_guessing_game():
    """
    A simple number guessing game that demonstrates Python fundamentals
    """
    print("*****Number Guessing Game*****")
    print("Im thinking of a number between 1 and 100.")

    # Variables and random number generation
    random_numer = random.randint(1, 100)
    initial_attempts = 0
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

# Execute the game
if __name__ == "__main__":
    number_guessing_game()