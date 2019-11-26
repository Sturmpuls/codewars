# https://www.codewars.com/kata/5508249a98b3234f420000fb
from math import ceil
from string import ascii_letters, ascii_lowercase, ascii_uppercase

def moving_shift(s, shift, reverse=False):

    caesar_string = ''
    increment = 1 if reverse is False else -1
    
    for letter in s:

        if letter in ascii_letters:
            idx = ascii_letters.index(letter) % 26
            idx_shift = (idx + shift) % 26

            if letter.islower():
                letter = ascii_lowercase[idx_shift]
            if letter.isupper():
                letter = ascii_uppercase[idx_shift]

        caesar_string += letter
        
        shift += increment

    parts = int(ceil(len(caesar_string)/5.0))
    
    caesar_list = [caesar_string[1*i:1*i+parts] for i in range(0, len(caesar_string), parts)]
    
    if len(caesar_list) < 5:
        for i in range(5 - len(caesar_list)):
            caesar_list.append('')
    
    return caesar_list

def demoving_shift(s, shift):
    s = ''.join(s)
    shift = 26-shift
    unshifted = ''.join(moving_shift(s, shift, reverse=True))
    return unshifted
