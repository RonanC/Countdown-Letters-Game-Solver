"""
countdown.nines
~~~~~~~~~~~~

This module creates the nines file and generates the random 9 letter word
"""

if __name__ != 'countdown' and __name__ != 'solver.nines':
    import solver
else:
    from solver import solver

import pickle
from random import choice, shuffle

def save_nines(words, filename, serialize=2):
    def pkl_words():
        pkl_filename = filename + '.pkl'
        output = open(pkl_filename, 'wb')
        pickle.dump(words, output)
        output.close()
        print("serialized words to ", pkl_filename)

    def txt_words():
        txt_filename = filename + '.txt'
        file = open(txt_filename, 'w')
        for word in words:
            file.write('%s\n' % word)
        file.close()
        print("saved words to ", txt_filename)

    if serialize == 0:
        pkl_words()
    elif serialize == 1:
        txt_words()
    else:
        pkl_words()
        txt_words()


def load_nines():
    if __name__ != 'countdown' and __name__ != 'solver.solver':
        # print('__name__: %s' % __name__)
        nines_list_file = "nines_list"
    else:
        nines_list_file = "solver/nines_list"

    # Load in nines_list (unpickle)
    nines_list_file += ".pkl"
    nines_list = pickle.load(open(nines_list_file, 'rb'))

    return nines_list


def word_picker():
    # picks a nine letter word, shuffles it, and returns it.
    nines_list = load_nines()
    word = choice(nines_list)
    lst_word = list(word)
    shuffle(lst_word)
    return ''.join(lst_word)


def gen_nines(length=9):
    # create a list of words
    word_list = solver.load_word_list()
    nines_list = []

    for num in range(0, len(word_list)):
        if len(word_list[num]) == length:
            nines_list.append(word_list[num])

    save_nines(nines_list, 'nines_list')


def main():
    print(word_picker())


if __name__ == '__main__':
    main()
