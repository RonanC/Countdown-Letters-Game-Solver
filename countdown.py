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
from solver import timing, solver, letter_gen
import sys


def main_menu():
    options = {
        0: quit, 1: create_word_list, 2: create_letters, 3: run_solver,
        4: time_solver, 5: time_preproc, 6: save_dict
    }

    prompt = '> '

    #  0: false
    # !0: true
    while 1:
        print('\n~~~~~Countdown~~~~~')
        print('~~~~~~~~~~~~~~~~~~~')
        print('1:\tCreate Word List')
        print('2:\tCreate Random Letters')
        print('3/ent:\tRun Solver')
        print('4:\tRun Solver (timed)')
        print('5:\tTime Preprocessing')
        print('6:\tCreate & Save dictionary')
        print('0:\tQuit\n')

        str_choice = input(prompt)
        if str_choice.isdigit():
            choice = int(str_choice)
            if choice < len(options) and choice >= 0:
                options[int(choice)]()
            else:
                print('Choices between 0 and %s.' % (len(options) - 1))
        elif str_choice == '':
            # enter key was pressed
            options[3]()
        else:
            print('Integers (or enter key) only.')


def run_solver():
    print('Running solver....')
    letters = letter_gen.letter_gen()
    print("Letters:\t%s" % letters)
    solver.find_anag(solver.load_word_dict(), letters, 1)


def time_solver():
    timing.time_solver()


def time_preproc():
    timing.time_preproccesing()


def save_dict():
    # loads word list, creates dictionary, saves it to pickle
    word_list = solver.load_word_list()
    word_dict = solver.create_word_dict(word_list)
    solver.save_word_dict(word_dict, 1, 0)


def create_letters():
    print('Creating random letters...')
    print(letter_gen.letter_gen())


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


def quit():
    print('Good bye.')
    sys.exit()


def main():
    main_menu()


if __name__ == '__main__':
    main()
