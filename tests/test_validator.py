import pytest
from bulls_and_cows.validator import is_valid_guess

def test_valid_guess():
    assert is_valid_guess("1234") is True
    assert is_valid_guess("9876") is True

def test_invalid_length():
    assert is_valid_guess("123") is False
    assert is_valid_guess("12345") is False

def test_non_digit_characters():
    assert is_valid_guess("12a4") is False
    assert is_valid_guess("1.23") is False
    assert is_valid_guess("abcd") is False

def test_starts_with_zero():
    assert is_valid_guess("0123") is False

def test_duplicate_digits():
    assert is_valid_guess("1123") is False
    assert is_valid_guess("1223") is False
    assert is_valid_guess("1233") is False
    assert is_valid_guess("4444") is False