"""liczby pierwsze to takie ktore maja tylko 2 naturalne dzielniki tj 1 i samą siebie
np. 2,3,5,7,9"""

def prime_nums(num: int) -> None:
    if num < 2:
        return False
    for counter in range(2, num):
        if num % counter == 0:
            return False

    return True


print(prime_nums(5))
print(prime_nums(1))
print(prime_nums(4))