### Ronan Connolly
#### G00274374
# Countdown-Letters-Game-Solver
A Python script that solves the Countdown letters game, and a readme explaining how the solver works.

## Introduction
This project was created as part of my Theory of Algorithms module in college.  
The basic project brief was to create an algorithm in Python to solve the Countdown Conundrum game where you have a nine letter word consisting of at least three vowels and four consonants.
The goal is to create the most efficient algorithm as possible, keeping track of different approaches, timing each algorithm, checking performance, memory usage and basically doing a lot of analysis.  
This project gives insight into really digging deep into algorithms and not just trying to create a complete solution but an optimal solution.  
All findings during analysis and through the progression of this project will be listed in this readme, in the commit history and in the issue tracker.  

Official Project Brief: [Project Brief][1]

## Background
### General Research
First I set up an issue tracker for my "General Python Research".  
This was my personal "preprocessing" step.  
Before I even began this project I spent quite some time studying python.  
I completed [Code Schools][2] "Try Python" and "Flying Through Python" courses.  
I also completed their python [screencast][3] which included using an external API via the HTTP requests library and the smtplib module.  
I watched some countdown episodes and read up on the rules to clarify some things and to get my program as close as possible to the real deal.

Listened to some [python podcasts][4], and read a few chapters from Miguels book on [Flask][5].  
Once all of this research was done, I went back through all the excercises done in class and modified them (they are located [here][6]).  
To finalise my research I completed the Gambit Problem Sheet in Python, located [here][7].

### Countdown Research
Now that the intense research is complete I went onto setup a list of project tasks to be completed in the github issue tracker.

The first task on the list was to Google "countdown letters game solver" and "python word permutations" .  
I found these relevant results:  
- [Ben Mason](http://benmason.net/countdown.qsp])
- [Incoherency](http://incoherency.co.uk/countdown/)
- [Data Genetics](http://www.datagenetics.com/blog/august52014/index.html)

Python algorithms already out there:
- [thesamovar algorithm](http://thesamovar.net/countdownnumbers)
- [thesamovar blog post](https://thesamovar.wordpress.com/2008/01/02/countdown-numbers-game-in-python/)
- [gossamer](http://www.gossamer-threads.com/lists/python/python/616211)
- [gossamer 2](http://www.gossamer-threads.com/lists/python/python/618568)
- [Stack Overflow](http://stackoverflow.com/questions/35640414/countdown-letters-solver-recursive-python)

I found this great paper on the countdown problem: [The countdown problem][8].

The second task was to read [heaps paper][9] on permutations and try to implement it in python.  
This helped me in understanding word permutations at a deeper level in Python.

### Coding it up

My third task was to get the wordlist, I decided to create a webscraper to do this for me.  
I used the [BeautifulSoup][10] package alongside the [Requests library][11] in order to download the various Oxford wordlists and parse them.  
I used this [tutorial][15] as a starting point.

The next task was to focus primarily on trying various techniques in order to find all of the words from the nine letters given.

Next I created a function to randomely select 9 letters (with at least 3 vowels and 4 consonants).

I then created a program that could load in my various different countdown solver packages, call them with the 9 letter module, and time them all automatically.

The cherry on top was to implement my packages into a flask application and host it on heroku.  

I updated this document constantly during my journey through this project.  
I added anything of interest or that stood out, be it big efficiency spikes or drawbacks that I came accross.  


## Words list
My words list is in the file [wordslist.txt][12] in this repoistory/gist.  
I got my words list from the [Oxford Learner's Dictionaries][13] website.  
In order to efficiently retrieve all the words from all the word lists on the website I create a web scraper which you can run from the menu in the main program.

I also considered creating an algorithm that parses all the words in a book and using that as a word list. I think Leo Tolstoy's *War and Peace* would suffice.

My web_scraper module loads in a list of base_urls and extensions. Next it creates all the full urls. Then each page of each url is checked, all words are made lower case and saved to a set (providing uniqueness). All the words per page are saved to the url words list. Once a url is fully checked that word list is merged into the main word list. 

My program downloads the Oxford3000, Academic, Pictures, Usage Notes, and New Words lists in both English and American English.

The words are then saved to a text and a pickle file, to be later utilized by the main program.

## Architecture/Structure
The main point of access for my program is `countdown.py` which is in the main folder.  
This file accesses the scripts in sub-directories, this keeps things modular and more pythonic.  
I added the `__init__.py` files to all sub-directories in order to let Python know these subdirectories are actually packages (I tested this and it is necessary).  
I used `if __name__ == '__main__` in order to allow the use of the sub-packages by themselves. This is needed when dealing with loading and saving files as the program will be checking only the main modules current directory.

## Letter Generator
The `letter_gen.py` module create a random nine letter list with at least three vowels and four consonants. I saved the string.ascii_lowercase to a list, I created a vowels list, I then used list comprehensions to add all items from the full letters list excluding the vowels:  
```py
consons = [x for x in letters if x not in vowels]
```

## Python script
My script is in the files [solver.py][14] in this repository and it works as follows.  
The most important section is:

```py
import random
print(random.shuffle("My code is cool."))
```

Previously it looked like this:
```py
# Note that the following snippet of code was adapted from
# the Stack Overflow post available here: http://www.so.com/post/123
import nothing
```
That didn't work too well, so I changed it.

## Step Through
*Step by step what the main module does*

## Preprocessing
My script does a lot of preprocessing, which only needs to be run once.  
Once the preprocessing is done we can run the game solver again and again without that overhead.

### 1: sorting with a dictionary
This version of the solver took the biggest preprocessing time.  
I like how simple and elegant this solution is.  
In order to have a list as the value of the dictionary I used the Python Collections - Default Dictionary. I found this great [Stack Overflow answer](http://stackoverflow.com/a/26367880/2052295).  
In added a list as the value type very simply:  
```py
word_dict = defaultdict(list)
```

One of the great things about this dictionary is that when you append the first word onto the list it automatically calls the `default_factory` which returns an empty list:  
```py
word_dict[srt_word].append(word)
```

## Efficiency
Here's some stuff about how efficient my code is, including an analysis of how many calculations my algorithm requires.

## Timing
*the results of all variations*

## Memory
*screen shots of memory usage*

## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Countdown letters game.

## References
[1]: https://gist.github.com/ianmcloughlin/cc5340ee080bd135919a
[[1]]: Project Brief

[2]: https://www.codeschool.com/learn/python
[[2]]: Codeschool Python Courses (2)

[3]: https://www.codeschool.com/screencasts/soup-to-bits-flying-through-python
[[3]]: Codeschool Python Screencast

[4]: https://talkpython.fm/
[[4]]: Python Podcast

[5]: http://shop.oreilly.com/product/0636920031116.do
[[5]]: Flask Web Development

[6]: http://comjnl.oxfordjournals.org/content/6/3/293.full.pdf
[[6]]: Lab Problems

[7]: http://www.crummy.com/software/BeautifulSoup/
[[7]]: Gambit Problem Sheet

[8]: http://www.cs.nott.ac.uk/~pszgmh/countdown.pdf
[[8]]: The Countdown Problem - Graham Hutton

[9]: http://comjnl.oxfordjournals.org/content/6/3/293.full.pdf
[[9]]: Permutations by interchanges - B. R. Heap

[10]: http://www.crummy.com/software/BeautifulSoup/
[[10]]: Beautiful Soup

[11]: http://requests.readthedocs.org/en/master/
[[11]]: Requests - The only Non-GMO HTTP library for Python

[12]: countdown/word_list.txt
[[12]]: wordlist.txt file

[13]: http://www.oxfordlearnersdictionaries.com/wordlist/
[[13]]: Wordlists in Oxford Learner's Dictionaries

[14]: solver.py
[[14]]: solver.py file

[15]: http://docs.python-guide.org/en/latest/scenarios/scrape/
[[15]]: HTML Scraping
