#!/usr/bin/python3

import re


def solution(s):
    rez = re.findall('..?', s)
    if len(rez) and len(rez[-1]) % 2 != 0:
        rez[-1] += '_'
    return rez


solution("asdfadsf")    # ['as', 'df', 'ad', 'sf']
solution("asdfads")     # ['as', 'df', 'ad', 's_']
solution("")            # []
solution("x")           # ["x_"]


# Not mine, but what I was looking for:

def solution(s):
    return re.findall(".{2}", s + "_")
