#!/usr/bin/python3

def to_jaden_case(string):
    jaden = ''
    for word in string.split():
        jaden += '%s ' % word.capitalize()
    return " ".join(jaden.split())  # Avoid last white space



def to_jaden_case(string):
    return (" ".join((w.capitalize()) for w in string.split()))


quote = "How can mirrors be real if our eyes aren't real"
to_jaden_case(quote)
