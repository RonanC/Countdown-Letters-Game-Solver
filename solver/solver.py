"""
countdown.solver
~~~~~~~~~~~~

This module finds all possible anagrams from a given list of letters.
It checks every possible permutation of the word aginst a dictionary.
A dictionary and a list of letters are given as arguments to the main module.

Once a permutation matches a word,
then all possible words from that permutation are returned.

This is due to the sorting of the works in the dictionary.
"""

# init
import pickle
from collections import defaultdict
if __name__ == '__main__':
    from letter_gen import letter_gen
    from permut import permut
else:
    from solver.letter_gen import letter_gen
    from solver.permut import permut


def load_word_list():
    if __name__ == "__main__":
        word_list_file = "../web_scraper/word_list"
    else:
        word_list_file = "web_scraper/word_list"

    # Load in word_list (unpickle)
    word_list_file += ".pkl"
    word_list = pickle.load(open(word_list_file, 'rb'))

    return word_list


def save_word_dict(word_dict, serialize=2):
    if __name__ == "__main__":
        filename = 'word_dict'
    else:
        filename = 'solver/word_dict'

    def pkl_words():
        pkl_filename = filename + '.pkl'
        output = open(pkl_filename, 'wb')
        pickle.dump(word_dict, output)
        output.close()
        print("serialized words to ", pkl_filename)

    def txt_words():
        txt_filename = filename + '.txt'
        file = open(txt_filename, 'w')
        for key, value in word_dict.items():
            file.write('%s\t%s\n' % (key, value))
        file.close()
        print("saved words to ", txt_filename)

    if serialize == 0:
        pkl_words()
    elif serialize == 1:
        txt_words()
    else:
        pkl_words()
        txt_words()


def load_word_dict():
    if __name__ == "__main__":
        word_dict_file = "word_dict"
    else:
        word_dict_file = "solver/word_dict"

    # Load in word_dict (unpickle)
    word_dict_file += ".pkl"
    word_dict = pickle.load(open(word_dict_file, 'rb'))

    return word_dict


def create_word_dict(word_list):
    word_dict = defaultdict(list)

    for word in word_list:
        srt_word = ''.join(sorted(word))
        word_dict[srt_word].append(word)

    return word_dict


def find_anag(word_dict, letters):
    word_permu = permut(letters)
    # print(word_permu)

    count = 0
    anagrams = 'empty'
    for word in word_permu:
        count += 1
        anagrams = word_dict.get(word, 'empty')
        if anagrams != 'empty':
            break

    print('Anagrams:\t%s' % anagrams)
    print('Attempts:\t%s\n' % count)


def solver():     
    # Create a new word dict
    # word_dict = create_word_dict(load_word_list())
    # Save word dict
    # save_word_dict(word_dict)

    # load dict
    word_dict = load_word_dict()

    # info
    # print("%s keys in the word dict.\n" % (len(word_dict)))

    # get random 9 letters
    letters = letter_gen()
    print('Letters:\t%s' % letters)

    # solver via dictionary and sorting
    find_anag(word_dict, letters)


def main():
    solver()

if __name__ == "__main__":
    main()
