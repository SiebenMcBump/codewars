#!/usr/bin/python3

def high_and_low(numbers):
    num = numbers.split()
    num.sort(key=int)
    numbers = "%s %s" % (num[len(num)-1], num[0])

    return numbers


high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5")  # return "5 -3"
high_and_low("1 9 3 4 -5")  # return "9 -5"


#NOTE: Can be shortened