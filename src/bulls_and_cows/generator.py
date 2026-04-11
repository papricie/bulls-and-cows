import random

def generate_secret_number() -> str:
    digits = list('0123456789')
    first_digit = random.choice(digits[1:])
    digits.remove(first_digit)
    secret = first_digit

    for _ in range(3):
        d = random.choice(digits)
        digits.remove(d)
        secret += d

    return secret