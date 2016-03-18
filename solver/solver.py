"""
countdown.solver
~~~~~~~~~~~~

This module finds all possible anagrams from a given list of letters.
It checks every possible permutation of the word aginst a dictionary.
A dictionary and a list of letters are given as arguments to the main module.
"""

# 1: dictionary
# preprocessing:
# sort word, add it to dictionary
# add all words to that key
# then when you sort a given word you will instantly have all anagrams
# save as text file and pickle files

# 2: try hashing

# 3: try finding all permutations
# then search each permutation in the dictionary

# 4: try heaps algorithm

# try lab problems

# do gambit worksheet

# init
import pickle
from collections import defaultdict
if __name__ == '__main__':
    from letter_gen import letter_gen
    from permut import permut
else:
    from solver.letter_gen import letter_gen
    from solver.permut import permut


def load_word_list(filename):
    # Load in word_list (unpickle)
    filename += ".pkl"
    word_list = pickle.load(open(filename, 'rb'))

    return word_list


def save_word_dict(filename, word_dict, serialize=2):
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


def add_dict_words(word_list):
    word_dict = defaultdict(list)

    for word in word_list:
        srt_word = ''.join(sorted(word))
        word_dict[srt_word].append(word)

    return word_dict


def solver_dict(word_list, letters):
    if __name__ == "__main__":
        word_dict_file = 'word_dict'
    else:
        word_dict_file = 'solver/word_dict'

    # go through each word
    word_dict = add_dict_words(word_list)

    # save dictionary
    save_word_dict(word_dict_file, word_dict)
    print("%s keys in the word dict.\n" % (len(word_dict)))

    # letters
    # srt_letters = sorted(letters)
    # str_letters = ''.join(srt_letters)

    # get all permutations of word
    # print(letters)
    word_permu = permut(letters)
    # print(word_permu)

    count = -1
    for word in word_permu:
        count += 1
        anagrams = word_dict.get(word, 'empty')
        if anagrams != 'empty':
            break

    print('Anagrams:\t%s' % anagrams)
    print('Count:\t\t%s\n' % count)
    

    # anagrams = word_dict.get(word, 'empty')

    # if anagrams != 'empty':
    #     print('Letters: %s' % str_letters)
    #     print('Anagrams:\t%s\n' % anagrams)
    # else:
    #     print("No anagrams found.\n")

    # find anagram
    # found = 0
    # attempt = 0
    # while not found:
    #     attempt += 1
    #     print('\nAttempt:\t%s' % (attempt))

    #     # check full 9 letters
    #     anagrams = word_dict.get(str_letters, 'empty')

        # check every possible permutation
        # starting at 9 and going down
        # we know the dictionary is sorted 
        # so we need to take off the front and end
        # example: from
        # sfrom: sfro, from
        #   from: fro, rom
        #       fro: fr, ro
        #           fr: f, r 
        #           ro: o, m
        #       rom: !ro, om
        #   sfro: sfr, !fro
        #       sfr: sf, !fr
        #           sf: s !f
        # 
        # conclusion, there are always two splits, the second split only ever keeps one variation
        # one unique and one shared
        
        # print('str_letters: %s' % str_letters)
        # if anagrams != 'empty':
        #     # print('Found one on attempt %s' % attempt)
        #     # print('Letters: %s' % str_letters)
        #     print('Anagrams:\t%s\n' % anagrams)
        #     found = 1
        # elif len(str_letters) == 0:
        #     found = 1
        #     print("No anagrams found.\n")
        # else:
        #     str_letters = str_letters[:-1]


def solver():
    # this solver function calls all the other solvers
    # It also times them all

    if __name__ == "__main__":
        word_list_file = "../web_scraper/word_list"
    else:
        word_list_file = "web_scraper/word_list"

    # load word list
    word_list = load_word_list(word_list_file)

    # get random 9 letters
    letters = letter_gen()
    print('Letters:\t%s' % letters)

    # solver via dictionary and sorting
    solver_dict(word_list, letters)


def run():
    solver()

if __name__ == "__main__":
    run()
