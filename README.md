# Countdown-Letters-Game-Solver
### Student name: Ronan Connolly
#### Student number: G00274374
A Python script that solves the Countdown letters game, and a readme explaining how the solver works.

## Introduction
Insert introduction here.  
[Project Brief](https://gist.github.com/ianmcloughlin/cc5340ee080bd135919a)


## Background
First I set up an issue tracker for my "General Python Research".
Before I even began this project I spent quite some time studying python.  
I completed (Code Schools)[1] "Try Python" and "Flying Through Python" courses.  
Listened to some python podcasts[2], and read a few chapters from Miguels book on Flask[3].  
Once all of this research was done, I went back through all the excercises done in class and modified them (they are located on this repo: ####).  
To finalise my research I completed the Gambit Problem Sheet in Python, located here: ####.  

Now that the intense research is complete I went onto setup a list of project tasks to be completed in the github issue tracker.

The first task on the list was to Google "countdown letters game solver" and "python word permutations" .
I found these relevant results: [Cool Project name][2] and [Cool Solver][3].

The second task was to read heaps paper on permutations and try to implement it in python.
This helped me in understanding word permutations at a deeper level in Python.

My third task was to get the wordlist, I decided to create a webscraper to do this for me.
I used the ### package in order to do this.
I found these links very useful:

The next task was to focus primarily on trying various techniques in order to find all of the words from the nine letters given.

Next I created a function to randomely select 9 letters (with at least 3 vowels and 4 consonants).

I then created a program that could load in my various different countdown solver packages, call them with the 9 letter module, and time them all automatically.

The cherry on top was to implement my packages into a flask application and host it on heroku.  

I updated this document constantly during my journey through this project.    
I added anything of interest or that stood out, be it big efficiency spikes or drawbacks that I came accross.  


## Words list
My words list is in the file [wordslist.txt](wordslist.txt) in this repoistory/gist.
I got my words list from the [Oxford Learner's Dictionaries][1] website.

## Python script
My script is in the files [solver.py](solver.py) in this repository and it works as follows.
The most important section is:

```python
import random
print(random.shuffle("My code is cool."))
```

Previously it looks like this:
```python
# Note that the following snippet of code was adapted from
# the Stack Overflow post available here: http://www.so.com/post/123
import nothing
```
That didn't work too well, so I changed it.

## Preprocessing
My script does a lot of preprocessing, which only needs to be run once.
Once the preprocessing is done we can run the game solver again and again without that overhead.

## Efficiency
Here's some stuff about how efficient my code is, including an analysis of how many calculations my algorithm requires.

## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Coutdown letters game.


## References
[1]: https://www.codeschool.com/learn/python
[2]: https://talkpython.fm/
[3]: http://shop.oreilly.com/product/0636920031116.do
