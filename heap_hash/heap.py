"""
heap_hash.heap
~~~~~~~~~

A Python implementation of Heaps algorithm.
Customised for my use.

This file must be run from countdown
(any folder above, as it needs access to the solver folder)
"""

from random import shuffle

# n = integer
# A = array (list)
perms = []


def gen_perms(n, A):
    """
    Recursively generates permutations.
    """
    if n == 1:
        perms.append(''.join(A))
        # print(A)
    else:
        for i in range(n-1):
            gen_perms(n-1, A)
            if (n % 2) == 0:
                A[i], A[n-1] = A[n-1], A[i]
            else:
                A[0], A[n-1] = A[n-1], A[0]
        gen_perms(n-1, A)


def heap(word):
    """
    Runs the module.
    """
    gen_perms(len(word), list(word))
    words = []
    # deep copy (rather then pointer)
    words[:] = perms[:]
    del perms[:]
    return words


def check_word(word_list, perm_list):
    """
    Pass in the word and permutations list.
    We check if any of the permutations are in the word list.
    We are using the nine letter word list.
    Both lists are hashes.
    """

    # print('word_list: %s' % len(word_list))
    # print('perm_list: %s' % len(perm_list))
    total_count = 0
    perm_count = 0
    word_count = 0

    for word_hash_num, word_value in word_list.items():
        word_count += 1
        perm_count = 0
        for perm_hash_num, perm_value in perm_list.items():
            total_count += 1
            perm_count += 1
            # print('perm: %s    word: %s    t_count:\t%s    p_count: %s    w_count: %s' % (perm_list[perm_hash_num], word_list[word_hash_num], total_count, perm_count, word_count))
            if perm_list[perm_hash_num] == word_list[word_hash_num]:
                print('Found a match:\t%s\tAfter checking %s words.' % (word_list[word_hash_num], total_count))
                return (word_list[word_hash_num], total_count)



def main():
    """
    Test function.
    """
    # word = 'accompany'
    word ='hello'
    word_lst = list(word)
    shuffle(word_lst)

    gen_perms(len(word_lst), list(word_lst))

    words = []
    words[:] = perms[:]
    del perms[:]

    print(words)
    print()
    print(len(words))


if __name__ == '__main__':
    main()
