#!/usr/bin/python3

def iq_test(numbers):
    num = {i: numbers.split()[i] for i in range(len(numbers.split()))}

    even = []
    odd = []

    for k, v in num.items():
        if is_even(v):
            even.append(k+1)
        else:
            odd.append(k+1)

    return compare(even, odd)


def is_even(i):
    return True if int(i) % 2 == 0 else False


def compare(even, odd):
    return odd[0] if len(even) > len(odd) else even[0]


iq_test("2 4 7 8 10")  # 3
iq_test("1 2 2")  # 1


# NOTE: Can be shortened
