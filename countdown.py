"""
countdown
~~~~~~~~~~~~

This is the main module.
It implements all other modules in this project.

This project:
- creates a dictionary
- generates a random list of letters
- tries to find all the anagrams in the list
- times the various anagram solvers
- prints an analysis of the results

See other module headers for more information.
"""

from web_scraper.web_scraper import web_scraper
from solver import timing, solver, letter_gen, nines
from heap_hash import heap, hashing
import sys
import timeit


def main_menu():
    options = {
        0: quit, 1: create_word_list, 2: create_letters, 3: save_dict,
        4: run_solver, 5: time_solver, 6: time_preproc,
        7: gen_save_nines, 8: get_nine, 9: run_solver_nine
    }

    prompt = '> '

    #  0: false
    # !0: true
    while 1:
        print('\n~~~~~Countdown~~~~~')
        print('~~~~~~~~~~~~~~~~~~~')
        print('Create:')
        print('1:\tCreate Word List')
        print('2:\tCreate Random Letters')
        print('3:\tCreate & Save dictionary')
        print('Solver:')
        print('4/ent:\tRun Solver')
        print('5:\tRun Solver (timed)')
        print('6:\tTime Preprocessing')
        print('Nines:')
        print('7:\tGen & Save Nine Letter Words')
        print('8:\tGet nine letter word')
        print('9:\tRun solver with nine letter word')
        print('Other:')
        print('a:\tHeap Hash Algorithm')
        print('0:\tQuit\n')

        str_choice = input(prompt)
        if str_choice.isdigit():
            choice = int(str_choice)
            if choice < len(options) and choice >= 0:
                options[int(choice)]()
            else:
                print('Choices between 0 and %s.' % (len(options) - 1))
        elif str_choice.strip().lower() == 'a':
            time_heap_hash()
        elif str_choice == '':
            # enter key was pressed
            options[4]()
        else:
            print('Integers (or enter key) only.')


# create:
def create_word_list():
    print('\nThis may take up to 2/3 mins to complete.')
    print('1:\tContinue')
    print('0:\tCancel')

    str_choice = input('> ')
    if str_choice.isdigit():
        choice = int(str_choice)
        if choice == 1:
            print('Creating dictionary...')
            web_scraper()
        else:
            print('Cancelled')
    else:
        print('Cancelled')


def create_letters():
    print('Creating random letters...')
    print(letter_gen.letter_gen())


def save_dict():
    # loads word list, creates dictionary, saves it to pickle
    word_list = solver.load_word_list()
    word_dict = solver.create_word_dict(word_list)
    solver.save_word_dict(word_dict, 1, 0)


# solver:
def what_dict():
    print('\nWhat dictionary?')
    print('1:\tOxford Learners (10938 words)')
    print('2:\tUnix (235886 words)')
    print('0:\tCancel')

    str_choice = input('> ')
    if str_choice.isdigit():
        choice = int(str_choice)
        if choice == 1:
            print('Oxford selected.')
        elif choice == 2:
            print('Unix selected.')
        else:
            print('Invalid, defaulting to Oxford')
            choice = 1
    else:
        print('Invalid, defaulting to Oxford')
        choice = 1

    return choice


def run_solver():
    dict_choice = what_dict()

    setup = """
if __name__ != 'countdown' and __name__ != 'timeit':
    import solver, letter_gen
    from unix_words import unix_words
else:
    from solver import solver, letter_gen
    from unix_words import unix_words

def run(dict_num):
    letters = letter_gen.letter_gen()
    print("Letters:\t%s" % (letters))

    if dict_num == 2:
        word_dict = unix_words.load_word_dict()
    else:
        word_dict = solver.load_word_dict()
    solver.find_anag(word_dict, letters, 1)
    """

    seconds = timeit.timeit(stmt='run(%s)' % dict_choice, setup=setup, number=1)
    print('Took %s seconds.' % (seconds))


def time_solver():
    dict_choice = what_dict()
    timing.time_solver(dict_choice)


def time_preproc():
    dict_choice = what_dict()
    timing.time_preproccesing(dict_choice)


# nines:
def gen_save_nines():
    print('Generating & saving nine letter words...')
    nines.gen_nines()


def get_nine():
    print('Nine letter word: %s' % nines.word_picker())


def run_solver_nine():
    print('Running solver with nine letter word (jumbled)....')
    # letters = nines.word_picker()
    # print("Letters:\t%s" % letters)

    setup = """
if __name__ != 'countdown' and __name__ != 'timeit':
    import solver, nines
else:
    from solver import solver, nines

def run():
    letters = nines.word_picker()
    print("Letters:\t%s" % (letters))
    solver.find_anag(solver.load_word_dict(), letters, 1)
    """

    seconds = timeit.timeit(stmt='run()', setup=setup, number=1)
    print('Took %s seconds.' % (seconds))


# other algorithms:
def time_heap_hash():
    setup = """
def run():
    run_heap_hash()
    """

    seconds = timeit.timeit(stmt='run()', setup=setup, number=1, globals=globals())
    print('Took %s seconds.' % (seconds))


def run_heap_hash():
    word = nines.word_picker()
    # print('Chosen word: %s\n' % word)

    nines_list = nines.load_nines()
    hash_nines_dict = hashing.hash_word_list(nines_list)

    perms = heap.heap(word)
    hash_perms_dict = hashing.hash_word_list(perms)

    print('Checking %s words in the dictionary against %s permutations of the chosen word: %s' % (len(hash_nines_dict), len(hash_perms_dict), word))
    heap.check_word(hash_nines_dict, hash_perms_dict)
    # print(match)
    # print('\nMatch: %s' % match)


# misc:
def quit():
    print('Good bye.')
    sys.exit()


def main():
    main_menu()


if __name__ == '__main__':
    main()
