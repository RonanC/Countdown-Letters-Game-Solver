"""
heap_hash.hashing
~~~~~~~~~

Permutation generator via a custom hashing algorithm
"""

import hashlib


def hash_word(word):
    """
    Hashes a word with md5.
    """
    word_hash = hashlib.md5(word.encode('utf-8')).hexdigest()
    return word_hash


def hash_word_list(word_list):
    """
    Turns a word list into a hashed dictionary.
    The key is the hash, the word is the value.
    """
    word_dict = {}
    for num in range(0, len(word_list)):
        word_str = ''.join(word_list[num])
        word_hash = hash_word(word_str)
        # print('str: %s\thash: %s' % (word_str, word_hash))
        word_dict[word_hash] = word_str

    return word_dict


def main():
    word = 'hello'
    hash_word(word)

if __name__ == '__main__':
    main()
