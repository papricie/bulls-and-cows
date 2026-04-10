from bulls_and_cows.generator import generate_secret_number
from bulls_and_cows.validator import is_valid_guess
from bulls_and_cows.evaluator import evaluate_guess

SEPARATOR = "-" * 50


def play_game() -> None:
    print("Welcome to Bulls and Cows!")
    print(SEPARATOR)

    secret = generate_secret_number()

    # DEBUG (později smažeme)
    print("Secret:", secret)

    while True:
        guess = input("Enter your guess: ")

        if not is_valid_guess(guess):
            print("Invalid input, try again.")
            continue

        bulls, cows = evaluate_guess(secret, guess)

        print(f"{bulls} bulls, {cows} cows")

        if bulls == 4:
            print("You won!")
            break