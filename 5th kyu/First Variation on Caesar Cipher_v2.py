# https://www.codewars.com/kata/5508249a98b3234f420000fb
from math import ceil
from string import ascii_lowercase as abc, ascii_uppercase as ABC

def _code(string, shift, mode):
    return ''.join(
        abc[(abc.index(c) + mode*i + shift) % len(abc)] if c in abc else
        ABC[(ABC.index(c) + mode*i + shift) % len(ABC)] if c in ABC else c
        for i, c in enumerate(string)
        )

def moving_shift(string, shift):
    encoded = _code(string, shift, 1)
    cut = int(ceil(len(encoded) / 5.0))
    return [encoded[i : i+cut] for i in range(0, 5 * cut, cut)]

def demoving_shift(array, shift):
    return _code(''.join(array), -shift, -1)
