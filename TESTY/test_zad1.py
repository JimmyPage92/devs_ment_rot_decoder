"""Zad 1.
Stwórz funkcję sprawdzającą, czy liczba jest pierwsza. Otestuj ją,
pamiętając równocześnie o otestowaniu każdego edge-case’a (np. 1 nie
jest liczbą pierwszą).
Spróbuj stworzone testy umieścić w klasie.
Uwaga:
Aby uruchomić testy znajdujące się w klasie, np. TestIsPrime, użyj
polecenia:
'>>> pytest tests/tests.py::TestIsPrime'
"""

from generator_prime_nums import prime_nums

class TestisPrime:

    def test_should_return_True_when_we_provide_5_in_function_prime_nums_as_a_argument_this_function(self):
        num = 5
        assert prime_nums(num) is True

    def test_should_return_False_when_we_provide_1_in_function_prime_nums_as_a_argument_this_function(self):
        num = 1
        assert prime_nums(num) is False

    def test_should_return_False_when_we_provide_4_in_function_prime_nums_as_a_argument_this_function(self):
        num = 4
        assert  prime_nums(num) is False