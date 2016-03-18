"""
countdown.letter_gen
~~~~~~~~~~~~

This module generates random letters.
Arguments such as how many letters,
and max/min of vowels and consonants may be given.

Brief states min 3 vowels, 4 consonants.
Total of 9 letters.
"""

import string
from random import choice, shuffle


def letter_gen():
    letters = list(string.ascii_lowercase)
    vowels = ['a', 'e', 'i', 'o', 'u']
    consons = [x for x in letters if x not in vowels]

    # print("%s\n%s\n%s\n" % (letters, vowels, consons))

    my_letters = []

    for x in range(0, 3):
        vowel = choice(vowels)
        my_letters.append(vowel)

    for x in range(0, 4):
        conson = choice(consons)
        my_letters.append(conson)

    for x in range(0, 2):
        letter = choice(letters)
        my_letters.append(letter)

    shuffle(my_letters)
    print('My Letters: ', my_letters, '\n')

    return my_letters


def run():
    letter_gen()


if __name__ == '__main__':
    run()
