from bulls_and_cows.generator import generate_secret_number
from bulls_and_cows.validator import is_valid_guess
from bulls_and_cows.evaluator import evaluate_guess

SEPARATOR = "-" * 50


def play_game() -> None:
    print("Welcome to Bulls and Cows!")
    print(SEPARATOR)

    secret = generate_secret_number()

    show_secret = False  # Set to True for debugging purposes

    if show_secret:
        print("Secret:", secret)

    try:
        while True:
            guess = input("Enter your guess (or press Ctrl+C to exit): ")

            if not is_valid_guess(guess):
                print("Invalid input: Please enter 4 unique digits, not starting with 0.")
                continue

            bulls, cows = evaluate_guess(secret, guess)

            print(f"{bulls} bulls, {cows} cows")

            if bulls == 4:
                print("Congratulations! You won!")
                break
    except KeyboardInterrupt:
        print("\nGame terminated by user. Goodbye!")
    except EOFError:
        print("\nInput stream closed. Goodbye!")