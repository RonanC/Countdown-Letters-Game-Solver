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

from web_scraper import web_scraper
from solver.letter_gen import letter_gen
from solver.solver import solver
import sys


def main_menu():
    options = {0: quit, 1: create_dict, 2: create_letters, 3: run_solvers}
    prompt = '> '

    #  0: false
    # !0: true
    while 1:
        print('\n~~~~~Countdown~~~~~')
        print('~~~~~~~~~~~~~~~~~~~')
        print('1:\tCreate Dictionary')
        print('2:\tCreate Random Letters')
        print('3/ent:\tRun Solvers')
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


def run_solvers():
    print('Running solvers....')
    solver()


def create_letters():
    print('Creating random letters...')
    print(letter_gen())


def create_dict():
    print('\nThis may take up to 2/3 mins to complete.')
    print('1:\tContinue')
    print('0:\tCancel')

    str_choice = input('> ')
    if str_choice.isdigit():
        choice = int(str_choice)
        if choice == 1:
            print('Creating dictionary...')
            web_scraper.run()
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
