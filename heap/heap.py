"""
heap.heap
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
        perms.append(A)
    else:
        for i in range(0, n):
            gen_perms(n-1, A)
            if (n % 2) == 0:
                temp = A[i]
                A[i] = A[n-1]
                A[n-1] = temp
            else:
                temp = A[0]
                A[0] = A[n-1]
                A[n-1] = temp
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
    """

    # print('word_list: %s' % len(word_list))
    # print('perm_list: %s' % len(perm_list))
    total_count = 0
    perm_count = 0
    word_count = 0

    for perm in range(0, len(perm_list)):
        perm_count += 1
        total_count += word_count
        word_count = 0
        perm_str = ''.join(perm_list[perm])
        for word in range(0, len(word_list)):
            word_count += 1
            print('perm: %s    word: %s    t_count:\t%s    p_count: %s    w_count: %s' % (perm_str, word_list[word], total_count, perm_count, word_count))
            if perm_str == word_list[word]:
                # print('Found a match:\t%s' % word)
                return word
                # break


def main():
    """
    Test function.
    """
    word = 'accompany'
    word_lst = list(word)
    shuffle(word_lst)

    gen_perms(len(word_lst), list(word_lst))

    words = []
    words[:] = perms[:]
    del perms[:]

    print(words)


if __name__ == '__main__':
    main()
