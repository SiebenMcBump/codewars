#!/usr/bin/python

import re


def validBraces(string):
    open = 0
    close = 0
    opening = '([{'
    closing = ')]}'
    opened = []
    closed = []

    for i in string:
        # string.count() ?
        if i in opening:
            open += 1
            opened.append(i)
        else:
            close += 1
            closed.append(i)

    if open != close:
        return False

    for i, brace in enumerate(opened):
        same = match(brace)
        if closed[-(i + 1)] not in same:
            return False

    return True


def match(test):
    plist = ['()', '[]', '{}']
    for arg in plist:
        if test in arg:
            return arg


validBraces('()')   # True
validBraces('[(])')  # False
validBraces('(}')  # False

validBraces('{}()[]')  # True
validBraces('([}{])')  #  False
validBraces('{}({})[]')  # True


def validBraces(string):
    plist = ['()', '[]', '{}']
    iter = len(string) / 2
    print(iter)
    i = 0

    while i < iter:
        for elem in re.findall('..', string):
            print(elem)
            if elem in plist:
                string = string.replace(elem, '')
            print(string)
        i += 1
        print(i)

    if i == iter:
        return False
    else:
        return True

    # while [((elem for elem in re.findall('..', string)) in plist)]:
    #     string = [string.replace(elem, '') for elem in plist if elem in string]


validBraces('{}({})[]')  # True
validBraces('{}()[]')  # True
validBraces('([}{])')  #  False


d = '([}{])'
plist = ['()', '[]', '{}']

for elem in re.findall('..', d):
    if elem in plist:
        print('pouet')


# NOTE : To finish
