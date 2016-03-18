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


def main():
    web_scraper.run()

if __name__ == '__main__':
    main()
