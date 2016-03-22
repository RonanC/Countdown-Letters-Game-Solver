"""
heap_hash.hashing
~~~~~~~~~

Permutation generator via a custom hashing algorithm
"""

import hashlib


def hash_word(word):
    word_hash = hashlib.md5(word.encode('utf-8')).hexdigest()
    return word_hash


def hash_word_list(word_list):
    word_dict = {}
    # print(word_list)
    # print('word list len: %s' % len(word_list))
    for num in range(0, len(word_list)):
        # print(''.join(word_list[num]))
        word_str = ''.join(word_list[num])
        # print('str: %s' % (word_str))
        word_hash = hash_word(word_str)
        # print('str: %s\thash: %s' % (word_str, word_hash))
        word_dict[word_hash] = word_str

    return word_dict


# def save_dict():
#     print('save dict')


# def load_dict():
#     print('load dict')


def main():
    word = 'hello'
    hash_word(word)

if __name__ == '__main__':
    main()