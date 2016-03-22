"""
unix_words.unix_words
~~~~~~~~~~~~~~~~~~~~~

This package is for loading and saving the large unix word list.
There are 235886 words in this text file.
"""

import pickle
from collections import defaultdict


def load_word_list(serialise=1):
    """
    Loads by text or pickle file.
    """
    if __name__ != 'countdown' and __name__ != 'unix_words.unix_words':
        # print('__name__: %s' % __name__)
        word_list_file = "unix_words_list"
    else:
        word_list_file = "unix_words/unix_words_list"

    def load_txt(word_list_file):
        word_list_file += '.txt'
        word_set = set()
        file = open(word_list_file, 'r')

        for line in file:
            # print (line, end='')
            word = line.strip()
            if word.isalnum():
                if word.islower():
                    word_set.add(word)
                else:
                    word_set.add(word.lower())

        return list(word_set)

    def load_pkl(word_list_file):
        word_list_file += ".pkl"
        return pickle.load(open(word_list_file, 'rb'))

    if serialise == 0:
        word_list = load_txt(word_list_file)
    elif serialise == 1:
        word_list = load_pkl(word_list_file)
    else:
        print('invalid choice')

    return word_list


def save_words(words):
    """
    Pickles the word list.
    """
    if __name__ != 'countdown' and __name__ != 'unix_words':
        filename = 'unix_words_list'
    else:
        filename = 'unix_words/unix_words_list'

    def pkl_words():
        pkl_filename = filename + '.pkl'
        output = open(pkl_filename, 'wb')
        pickle.dump(words, output)
        output.close()
        print("serialised words to ", pkl_filename)

    pkl_words()


def create_word_dict(word_list):
    """
    Creates a word dictionary.
    """
    word_dict = defaultdict(list)

    for word in word_list:
        srt_word = ''.join(sorted(word))
        word_dict[srt_word].append(word)

    return word_dict


def save_word_dict(word_dict, show_output=1, serialize=2):
    """
    Saves the dictionary in pickle or text format.
    """
    if __name__ != 'countdown' and __name__ != 'unix_words':
        filename = 'unix_words_dict'
    else:
        filename = 'solver/unix_words_dict'

    def pkl_words():
        pkl_filename = filename + '.pkl'
        output = open(pkl_filename, 'wb')
        pickle.dump(word_dict, output)
        output.close()
        if show_output == 1:
            print("serialized words to %s" % pkl_filename)

    def txt_words():
        txt_filename = filename + '.txt'
        file = open(txt_filename, 'w')
        for key, value in word_dict.items():
            file.write('%s\t%s\n' % (key, value))
        file.close()
        if show_output == 1:
            print("saved words to %s" % txt_filename)

    if serialize == 0:
        pkl_words()
    elif serialize == 1:
        txt_words()
    else:
        pkl_words()
        txt_words()


def load_word_dict():
    """
    Loads the word dictionary.
    """
    if __name__ != 'countdown' and __name__ != 'unix_words.unix_words':
        print('__name__: %s' % __name__)
        word_dict_file = "unix_words_dict"
    else:
        word_dict_file = "unix_words/unix_words_dict"

    # Load in unix_word_dict (unpickle)
    word_dict_file += ".pkl"
    unix_word_dict = pickle.load(open(word_dict_file, 'rb'))

    return unix_word_dict


def main():
    """
    Test function.
    """
    words = load_word_list(1)
    unix_word_dict = create_word_dict(words)
    save_word_dict(unix_word_dict)
    print('done')
    # save_words(words)


if __name__ == "__main__":
    main()
