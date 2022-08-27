#potegowanie dwoch dodatnich liczb
#faza zielona

import typing as tp

def calc_power_two_positive_nums(num,exponent):
    return num**exponent

print(calc_power_two_positive_nums(2,2))

#potegowanie dwoch ujemnych liczb

def calc_power_two_negative_nums(num,exponent):
    return num**exponent


print(calc_power_two_negative_nums(-2,-2))

#potegowanie kiedy wykladnikiem jest0


def calc_power_when_exp_is_0(base,exp):

    return base**exp

print(calc_power_when_exp_is_0(2,0))

#potegowanie kiedy podstawa potegi jest 0


def calc_power_when_base_is_0(base,exp):
    return base**exp

print(calc_power_when_base_is_0(0,10))
print(calc_power_when_base_is_0(0,4))

#potegowanie kiedy wykladniiem jest ułamek

def calc_power_when_exp_is_float(base,exponent):
    return base**exponent

print(calc_power_when_exp_is_float(100,0.5))

print("------------")

def sum_of_arithmetic_sequence(start: int,end: int)-> None:
    suma = 0

    for num in range(start,end + 1):

        suma += num

    return suma

print(sum_of_arithmetic_sequence(1,10))
print(sum_of_arithmetic_sequence(10,15))


