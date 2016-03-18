"""
countdown.web_scraper
~~~~~~~~~~~~

This module searches the oxford learners dictionary website,
pulls down all word lists,
and combines them into one large dictionary.

References:
http://docs.python-guide.org/en/latest/scenarios/scrape/
"""

import requests
from bs4 import BeautifulSoup


def get_word_list(url):
    print("At url: ", url)
    url += '/?page='
    words = set()

    # check each page until we get a null ul
    pageNum = 0
    list_empty = 0
    while list_empty == 0:
        pageNum += 1

        html_doc = requests.get(url + str(pageNum)).text
        soup = BeautifulSoup(html_doc, 'html.parser')

        item_list = soup.find_all('ul')[4]

        if item_list.text.split():
            print('Page num: ', str(pageNum))
            for item in item_list.find_all('a'):
                # excludes any word with a space,
                # hyphen or other non alpha-numeric
                if item.text.isalnum():
                    # using lower here as there are duplicates otherwise
                    # also to keep the set cleaner
                    words.add(item.text.lower())
        else:
            list_empty = 1

    print('Words Found: ', len(words), '\n')
    return words


def main():
    url_list = []
    word_set = set()
    base_url = 'http://www.oxfordlearnersdictionaries.com'
    base_url += '/wordlist'
    # /english/oxford3000

    # lang
    f = open('url_lang.txt', 'r')
    url_lang = []
    for line in f:
        url_lang.append(line.strip())
    f.close()

    #  label
    f = open('url_label.txt', 'r')
    url_label = []
    for line in f:
        url_label.append(line.strip())
    f.close()

    #  category
    f = open('url_categ.txt', 'r')
    url_categ = []
    for line in f:
        url_categ.append(line.strip())
    f.close()

    for label in url_label:
        for lang in url_lang:
            for categ in url_categ:
                new_url = base_url + lang + label + categ
                url_list.append(new_url)

    for url in url_list:
        word_set = set(list(word_set) + list(get_word_list(url)))

    # words_sorted = sorted(list(word_set), key=lambda s: s.lower())
    words_sorted = sorted(list(word_set))

    print(words_sorted, '\n')
    print('Total Words Found: ', len(words_sorted), '\n')

main()
