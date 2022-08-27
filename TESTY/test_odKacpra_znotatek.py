import pytest
from operations import *

#tworzymy testy do operacji potegowania
# A to jest podstawa potegi a n to wykladnik potegi
#1 poprawność wyniku dla wykładników będącymi całkowitymi wartościami dodatnimi

def test_should_return_4_num_operations_power_two_positive_nums():
    num = 2
    exponent = 2


    assert calc_power_two_positive_nums(num,exponent) == 4


# 2poprawność wyniku dlawykładników będącymi całkowitymi wartościami ujemnymi

def test_should_return_one_fourth_num_operations_power_two_negative_nums():
    num = -2
    exponent = -2

    assert calc_power_two_negative_nums(num,exponent) == 0.25

# 3 poprawność wyniku dlawykładników będącymi ułamkami

def test_should_return_1_for_0_exp():
    base = 10
    exp = 0

    assert calc_power_when_exp_is_0(base,exp) == 1

def test_should_return_0_for_0_base():

    base = 0 #podstawapotegi
    exp_1 = 40
    exp_2 = 4

    assert calc_power_when_base_is_0(base,exp_1) == 0
    assert calc_power_when_base_is_0(base,exp_2) == 0


def test_should_return_10_when_exponent_is_float():
    base = 100
    exponent = 0.5

    assert calc_power_when_exp_is_float(base,exponent) == 10


def test_should_return_55_for_sum_of_the_arithmetic_sequence():
    start = 1
    end = 10

    assert sum_of_arithmetic_sequence(start,end) == 55

    start = 10
    end = 15

    assert sum_of_arithmetic_sequence(start,end) == 75










