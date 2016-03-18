"""
countdown.web_scraper
~~~~~~~~~~~~

This module searches the oxford learners dictionary website,
pulls down all word lists,
and combines them into one large dictionary.

All words are unique and lowercase.
Words are gathered from the url_list textfile.

Once processing is complete the wordlist
it saved to a pickle and a text file.
"""

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    from save_words import save_words
else:
    from web_scraper.save_words import save_words


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

        try:
            item_list = soup.find_all('ul')[4]
        except Exception as e:
            print("exception: ", e)
            list_empty = 1
        else:
            if item_list.text.split():
                print('Page num: ', str(pageNum))
                for item in item_list.find_all('a'):
                    # excludes any word with a space,
                    # hyphen or other non alpha-numeric
                    if item.text.isalnum():
                        # using lower here as there are duplicates otherwise
                        # also to keep the set cleaner

                        # There are some groups and placenames like YMCA
                        # To remove these then edit the line below to 
                        # ignore words with caps
                        if item.text.islower():
                            words.add(item.text)
                        else:
                            # print(item.text)
                            words.add(item.text.lower())
            else:
                list_empty = 1
        # finally:
            #  uncomment in order to check all urls
            #  will only add first page of each
            # list_empty = 1

    print('Words Found: ', len(words), '\n')
    return words


def get_new_words(base_url):
    words = set()
    url = base_url + '/new_words'

    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser')

    try:
        item_list = soup.dd
    except Exception as err:
        print(err)
    else:
        if item_list.text.split():
            for item in item_list.find_all('a'):
                if item.text.isalnum():
                    words.add(item.text.lower())

    print('New Words Found: ', len(words), '\n')
    return words


def get_url_list(base_url, url_file):
    url_list = []
    file = open(url_file, 'r')

    url_items = []
    for line in file:
        exts = [x.strip() for x in line.split(',')]
        url_items.append(exts)
    file.close()

    for item in url_items:
        for categ in item[1:]:
            new_url = base_url + item[0] + categ
            url_list.append(new_url)

    return url_list


def get_words(base_url, url_list):
    word_set = set()

    # for url in url_list:
        # word_set = set(list(word_set) + list(get_word_list(url)))

    # the new words page has a different structure
    word_set = set(list(word_set) + list(get_new_words(base_url)))

    # words_sorted = sorted(list(word_set), key=lambda s: s.lower())
    words_sorted = sorted(list(word_set))

    print(words_sorted, '\n')
    print('Total Words Found: ', len(words_sorted), '\n')

    return words_sorted


def web_scraper():
    base_url = 'http://www.oxfordlearnersdictionaries.com'
    base_url += '/wordlist'

    # url list
    if __name__ == "__main__":
        url_file = 'url_list.txt'
        filename = 'word_list'
    else:
        url_file = 'web_scraper/url_list.txt'
        filename = 'web_scraper/word_list'

    url_list = get_url_list(base_url, url_file)
    words_sorted = get_words(base_url, url_list)
    save_words(words_sorted, filename)


def run():
    web_scraper()

if __name__ == "__main__":
    run()
