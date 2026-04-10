from bulls_and_cows.evaluator import evaluate_guess


def test_repeated_digits_guess():
    bulls, cows = evaluate_guess("1234", "1122")
    assert bulls == 1
    assert cows == 1


def test_reverse_number():
    bulls, cows = evaluate_guess("1234", "4321")
    assert bulls == 0
    assert cows == 4


def test_partial_overlap():
    bulls, cows = evaluate_guess("1234", "1299")
    assert bulls == 2
    assert cows == 0