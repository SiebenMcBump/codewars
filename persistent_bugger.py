#!/usr/bin/python3

from functools import reduce


def persistence(n):
    iter = 0
    i = list(map(int, str(n)))
    while len(i) > 1:
        i = list(map(int, str(reduce((lambda x, y: x * y), i))))
        iter += 1

    return iter


persistence(39)  # => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
# and 4 has only one digit.

persistence(999)  # => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
# 1*2*6 = 12, and finally 1*2 = 2.

persistence(4)  # => 0   # Because 4 is already a one-digit number.


# NOTE: Meh, I really don't like this one... Hardly readable.
# Must find a better way to practice map and lambda.
