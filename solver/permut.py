"""
solver.permut
~~~~~~~

This module sorts the letters and
saves every unique word to a list
then it orders the list by string length

It expects a list of letters.
"""

words = set()
# count = []


def permuter(letters):
    words.add(letters)
    # count.append(letters)
    if len(letters) > 1:
        permuter(letters[:-1])
        permuter(letters[1:])


def permut(letters):
    srt_lttrs = ''.join(sorted(letters))
    permuter(srt_lttrs)

    # sort by letters
    srt_words = sorted(list(words))

    # This tells the sort method to order
    # based on whatever the key function returns
    srt_words.sort(key=lambda s: len(s), reverse=1)

    # Needs to be cleared, otherwise is grows
    # as countdown.py calls it
    words.clear()

    # result
    return srt_words


def main():
    letters = 'eeeffffee'
    permuts = permut(letters)
    print(len(permuts))
    print(permuts)
    # print(len(count))


if __name__ == '__main__':
    main()