"""Zad 2.
Napisz funkcję, która zwracać będzie “Fizz”, gdy prześlesz do niej
wartość podzielną przez 3, “Buzz”, gdy podzielną przez 5, a “FizzBuzz”,
gdy liczba będzie podzielna przez obie te wartości. Napisz do niej testy
jednostkowe."""

from fizzbuzz_func import fizz_buzz

def test_should_return_Fizz_when_we_provide_in_function_num_divide_by_3():
    # wartosc podzielna przez 3 czyli np.9 bo jak dalem 15 to bylo zle

    assert fizz_buzz(num = 9) == "Fizz"

def test_should_return_Buzz_when_we_provide_in_function_num_divide_by_5():
    #wartosc podzielna przez 5 np 20 NIE 15

    assert fizz_buzz(num = 20) == "Buzz"

def test_should_return_Fizzbuzz_when_we_provide_in_function_num_divide_by_5_and_3():
    # wartosc podzielna przez 3 i 5 np 45

    assert fizz_buzz(num = 15) == "Fizzbuzz"

def test_should_return_num_when_we_provide_in_function_num_not_divide_by_5_and_3():
    # np. 4 i zwroci 4

    assert fizz_buzz(num = 4) == 4
