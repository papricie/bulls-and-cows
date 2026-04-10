def evaluate_guess(secret: str, guess: str) -> tuple[int, int]:
    bulls = 0
    cows = 0

    secret_used = [False] * 4
    guess_used = [False] * 4

    # 1. bulls
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
            secret_used[i] = True
            guess_used[i] = True

    # 2. cows
    for i in range(4):
        if guess_used[i]:
            continue

        for j in range(4):
            if not secret_used[j] and guess[i] == secret[j]:
                cows += 1
                secret_used[j] = True
                break

    return bulls, cows