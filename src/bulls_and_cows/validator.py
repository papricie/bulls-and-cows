def is_valid_guess(guess: str) -> bool:
    if len(guess) != 4:
        return False
    
    if not guess.isdigit():
        return False
    
    if guess[0] == "0":
        return False
    
    if len(set(guess)) != 4:
        return False
    
    return True