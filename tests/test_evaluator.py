import pytest
from bulls_and_cows.evaluator import evaluate_guess

@pytest.mark.parametrize("secret, guess, expected_bulls, expected_cows", [
    ("1234", "1234", 4, 0),  # Perfect match
    ("1234", "4321", 0, 4),  # All correct, wrong positions
    ("1234", "1299", 2, 0),  # Partial match positions
    ("1234", "5678", 0, 0),  # No match
    ("1234", "1122", 1, 1),  # Edge case: repeats (though validator stops this)
    ("4271", "1234", 1, 2),  # Random middle case
])
def test_evaluate_guess(secret, guess, expected_bulls, expected_cows):
    bulls, cows = evaluate_guess(secret, guess)
    assert bulls == expected_bulls
    assert cows == expected_cows