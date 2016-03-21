"""
countdown.timing
~~~~~~~~~~~~

This module times the various anagram solvers.
"""

import timeit
if __name__ != 'countdown' and __name__ != 'solver.timing':
    import solver
else:
    from solver import solver

# word_dict = solver.load_word_dict()


def time_preproccesing(num_times=1):
    # print('__name__: %s' % __name__)
    setup = """
if __name__ != 'countdown' and __name__ != 'timeit':
    import solver
else:
    from solver import solver

def run():
    word_list = solver.load_word_list()
    word_dict = solver.create_word_dict(word_list)
    """

    t = timeit.Timer(stmt='run()', setup=setup)
    time = t.timeit(num_times)
    print('loaded wordlist and created dictionary %s time(s)' % num_times)
    print('took %s seconds' % time)


def time_solver():
    show_output = 0
    print('With or without print output?')
    print('1/ent:\tWithout Print')
    print('2:\tWith Print')
    str_choice = input('> ')
    if str_choice.isdigit():
        choice = int(str_choice)
        if choice == 1:
            show_output = 0
        elif choice == 2:
            show_output = 1
        else:
            print('Cancelled')
    elif str_choice == '':
        show_output = 0
    else:
        print('Cancelled')

    num_def = 1000
    num_min = 1
    # 10 billion
    # 10'000'000'000
    num_max = 10000000000
    print('Run solver how many times?')
    print('Choose a number between %s and %s' % (num_min, num_max))
    print('Press enter to run default (%s)' % num_def)

    setup = """
if __name__ != 'countdown' and __name__ != 'solver.timing':
    import solver
    import letter_gen
else:
    from solver import solver, letter_gen

def run(show_output):
    letters = letter_gen.letter_gen()
    if show_output == 1:
        print(letters)
    solver.find_anag(word_dict, letters, show_output)
    """

    # We cannot pass the word_dict into the timer statement
    # So we make it global here
    # Globals are generally not recommended
    # as they can give strange behavior
    global word_dict
    word_dict = solver.load_word_dict()

    stmt = 'run(%s)' % (show_output)
    t = timeit.Timer(stmt=stmt, setup=setup, globals=globals())

    str_choice = input('> ')
    if str_choice.isdigit():
        choice = int(str_choice)
        if choice >= num_min and choice <= num_max:
            print('Took %s seconds.' % t.timeit(choice))
        else:
            print('Cancelled')
    elif str_choice == '':
        print('Took %s seconds.' % t.timeit(num_def))
    else:
        print('Cancelled')


def main():
    time_solver()

if __name__ == '__main__':
    main()
