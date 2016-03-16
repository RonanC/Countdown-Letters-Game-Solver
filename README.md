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

Offical Project Brief: [Project Brief][1]

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
- 

I found this great paper on the countdown problem: [The countdown problem][http://www.cs.nott.ac.uk/~pszgmh/countdown.pdf].

The second task was to read [heaps paper][8] on permutations and try to implement it in python.  
This helped me in understanding word permutations at a deeper level in Python.

### Coding it up

My third task was to get the wordlist, I decided to create a webscraper to do this for me.  
I used the [BeautifulSoup][9] package in order to do this.  
I also considered using the HTTP [Requests library][10] in order to download a wordlist file from a webpage via a HTTP Get request.

The next task was to focus primarily on trying various techniques in order to find all of the words from the nine letters given.

Next I created a function to randomely select 9 letters (with at least 3 vowels and 4 consonants).

I then created a program that could load in my various different countdown solver packages, call them with the 9 letter module, and time them all automatically.

The cherry on top was to implement my packages into a flask application and host it on heroku.  

I updated this document constantly during my journey through this project.  
I added anything of interest or that stood out, be it big efficiency spikes or drawbacks that I came accross.  


## Words list
My words list is in the file [wordslist.txt][11] in this repoistory/gist.  
I got my words list from the [Oxford Learner's Dictionaries][12] website.  
In order to efficiently retrieve all the words from all the word lists on the website I create a web scraper which you can run from the menu in the main program.  
I also considered creating an algorithm that parses all the words in a book and using that as a word list. I think Leo Tolstoy's *War and Peace* would suffice.

## Python script
My script is in the files [solver.py][13] in this repository and it works as follows.  
The most important section is:

```python
import random
print(random.shuffle("My code is cool."))
```

Previously it looked like this:
```python
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

[8]: http://comjnl.oxfordjournals.org/content/6/3/293.full.pdf
[[8]]: Permutations by interchanges - B. R. Heap

[9]: http://www.crummy.com/software/BeautifulSoup/
[[9]]: Beautiful Soup

[10]: http://requests.readthedocs.org/en/master/
[[10]]: Requests - The only Non-GMO HTTP library for Python

[11]: wordlist.txt
[[11]]: wordlist.txt file

[12]: http://www.oxfordlearnersdictionaries.com/wordlist/
[[12]]: Wordlists in Oxford Learner's Dictionaries

[13]: solver.py
[[13]]: solver.py file
