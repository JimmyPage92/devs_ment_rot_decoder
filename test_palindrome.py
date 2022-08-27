# TDD -> Test driven development (RED -> GREEN -> REFACTOR)
import pytest  # na szaro bo sie nie uzywa

from palindrome_generator import generate_palindrome


def test_palindrome_for_word_kajak():
    assert generate_palindrome(user_input="kajak") is True


def test_palindrome_for_word_monitor():
    assert generate_palindrome(user_input="monitor") is False

