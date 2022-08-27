#funkcja fizz_buzz

import typing as tp

def fizz_buzz(num: int) -> tp.Union[str,int]:
    if num % 3 == 0 and num % 5 == 0:
        return "Fizzbuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return num

print(fizz_buzz(9))
print(fizz_buzz(20))
print(fizz_buzz(15))
print(fizz_buzz(4))