"""
Saves the word list serialized and/or as a text file.
"""

import pickle


def save_words(words, filename, serialize=2):
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
