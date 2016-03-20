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

It takes approximately 2 to 3 minutes to download, analyse, clean, sort and pickle/txt the data.

Altough the saving of the end result (word list) is almost instantaneous.

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

## Permutation Generator
I created a module for generating all possible permutations of a sorted word.  
My script is in the [permut.py][16] file, inside the [solver][17] directory.
This doesn't take long since the word is sorted.  
Taking some inspiration from *Scheme* I created a recursive function.

First we create a global set:  
```py
words = set()
```

Next we have the recursive function:
```py
def permuter(letters):
    words.add(letters)
    if len(letters) > 1:
        permuter(letters[:-1])
        permuter(letters[1:])
```
This function adds each letter to the set.  
While testing I found that there were a few duplicates when using the list.  
Using a set prevents this with it's in built, highly efficient membership testing.  
Due to the fact the the word is sorted we only need to check a smaller sub set of the word, either clipping the front letter or the rear letter.

If I used a list and tweaked this algorithm it would be more efficient.  
After much time I could not figure it out.

## Python script
### Main module (countdown.py)
My script is in the files [countdown.py][14] in this repository and it works as follows.  
It is the main entry point for the program, although you can run each module independently thanks to the structuring.  

When you run this module you will be presented with a menu (~'s through the MD off so I took them out'):  
```
------Countdown-----
--------------------
1:  Create Dictionary
2:  Create Random Letters
3:  Run Solvers
0:  Quit
```

This lets you:  
- create a dictionary which runs the web scraper.
- test the random letters generator (which the run solvers option uses).
- run the solver (main algorithm) which will generate random letters and find the best match.

The solver function stops once it finds the best match, but it can keep going if we want, we just need to remove the break statement and append each results to a list.  

I decided that this was not necessary.

### Solver.py
This is where the action happens

First we get all the permutations as described above:

```py
def find_anag(word_dict, letters):
    word_permu = permut(letters)
    # print(word_permu)

    count = -1
    anagrams = 'empty'
    for word in word_permu:
        count += 1
        anagrams = word_dict.get(word, 'empty')
        if anagrams != 'empty':
            break

    print('Anagrams:\t%s' % anagrams)
    print('Attempts:\t%s\n' % count)
```
We can view the permutations by uncommenting the commented line.
Here we are keeping track of how many attempts it took before we found our word.

After running it many times I found it usually take 20 attempts but outliers of 3 and 34 attempts do pop up often. 

Since we are using the Oxford word lists, we only have approxiately 10'000 words so there are time we cannot find an anagram.  Altough this is rare as we are allowing the letters 'I' and 'a' as words.

If there are no anagrams then there will be 43 attempts.

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
*Step by step the logic of the solver*  
*Keep it succinct*

## Preprocessing
My program does a lot of preprocessing.  
There are a few generated files that are already processed, which are serialized via pickle, these files are loaded in which saves much time.

When running the program (with defaults of loading serialized data in via pickle) then the only processing that takes place is the permutations on the sorted word and the search of the max 30 possible keys in the dictionary.  
This is extremely fast. Due to the fact that the dictionary already has all the possible permutations stored at a key of the sorted word.  
The word list used by the dictionary generator is also saved via pickle which makes the dictionary generation even quicker.  

For more information on the word list check out the `Words list` heading above.

## Solver Algorithms (versions)
I decided to set my self the task of creating three different solver algorithms.  Since this project is all about the theory of algorithms I thought it would be worth while to cover not just the depth of algorithms but breadth as well. I feel like this is advantageous due to the fact that when you are faced with the same algorithm for days on end you can develop tunnel vision. By switching to another style of algorithm and coming up with new insights, by the time I finish up and revisit the previous algorithm there will more then likely be a Eureka moment.

### Sorted words in dictionary (final/main algorithm)
This version of the solver took the biggest preprocessing time, as the whole words list needed be sorted, turned into a dictionary and pickled.
Once complete we can reap the rewards of a much lower permutation check on any given word.

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

As stated previously there are a few duplicates created with the `permut.py` function, this is why I used a set. 

I counted the number of permutations against the number of permutations generated.
For a nine letter word I am generating 511 permutations, so there are duplicates. Only approximately 44 of these are used (including one character words). If a letter is duplicated then it affects the outcome of useful permutations.

511 permutations is not a lot due to the fact that my word is sorted, still I feel like there is a better solution then 511 attempts, also this does not scale into other (non sorted) algorithms.

**Maximum**
If all the letters are different then we are left with a maximum of 44 permutations.

**Minimum:**
If all the vowels are the same and the consonants also the same then we have:
27 permutations if 3 vowels and 6 consonants.
29 permutations if 4 consonants 5 vowels.

### Custom hashing
*TODO*

### Heaps algorithm (customized)
*TODO*

### conclusion
The sorted words in a dictionary ended up being the fasted, due mainly in part to the preprocessing and small dictionary size, however if you have a very large dictionary (that changes over time) and need to only calculate anagrams for a small number of jumbled words then the **custom hashing** would be better suited, but this is a very limited scenario.

If the use case of this algorithm is to be a web/mobile app where users input letters and get anagrams then the sorted dictionary processing algorithm is better as we will only need to do the preprocessing once and will be serving many requests (among all the users).

Even if it was an offline application the preprocessing is still okay as we can pickle (serialize) the dictionary before putting the application on the store.

If the dictionary cannot be saved and we must process all the words for each single request, then this algorithm is less viable.


### Efficiency
I've talked about the pre-processing and algorithms above.
I mentioned how many calculations my permutations algorithm takes.

Here I will go through the time each algorithm takes, and how much CPU and memory each uses.
If no algorithm is mentioned then I am speaking about he sorted word dictionary.

If the show flag is set to 1, an if statement will show the output of the letters, found anagrams, and number of attempts.
When running the algorithm for the defaulted 1000 times this if statement is ran each time.

I removed the if statement and it had made no effect to the performance.

## Timing
### Preproceesing time
This involves loading in the word dictionary (unpickle/unserialize),
Sorting each word, finding each permutation of that sorted word (discussed above under the *Sorted words in dictionary* heading),
and then finally creating the dictionary by using the sorted word as the key.

This takes `0.02294115200129454` seconds.
You should take into account that the total words in the Oxford Word Lists are approx 11,000.

####V1 - Sorted Word Dictionary
This was my original analysis where I printed 1000 and 10,000 times.
I tested it with output on and off.

**With print (1,000):**
```
11.675327009000284
11.296415551000337
11.303801694000413
```

**Without print (1,000):**
```
9.122691438999937
9.29408249900007
9.137007385999823
```

**With print (10,000):**
```
111.1710740339995
```

**Without print (10,000):**
```
95.93674115300018
```

We can see a clear difference when turning off the print statements.

###V2 - removed dict load
I the realized that I was loading the dictionary in each time.
This is part of the preprocessing.
I was shocked at the improvements.

**With print (1,000):**
```
0.5546017859996937
0.5734935639993637
0.5514507379994029
```

22 times faster (11 / 0.5)

**Without print (1,000):**
```
0.2962503909984662
0.3058995000028517
0.30122587000005296
```

Here we noticed a bigger difference in the output being turned off.
30 times faster (9 / 0.3)

**With print (10,000):**
```
6.038021037998988
6.296833869000693
5.4718684629988275
6.244787717998406
```

18 times faster (111 / 5)

**Without print (10,000):**
```
3.0099240979980095
2.9975806299989927
2.9792075869991095
2.9062734180006373
2.9962728889986465
```

32 times faster (96 / 3).

### if statements for output removed
We do not see any difference. 

**Without print (1,000):**
```
0.30075044499972137
0.28801490999831003
0.32457313800114207
```

**Without print (10,000):**
```
3.030269856000814
2.984034207998775
2.959833992001222
3.0004114049988857
```

## Memory
*screen shots of memory usage*

## Results
The countdown games give it's players 30 seconds to find the best anagram.

My script finds the answers in:

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

[14]: https://github.com/RonanC/Countdown-Letters-Game-Solver/blob/master/countdown.py
[[14]]: solver.py file

[15]: http://docs.python-guide.org/en/latest/scenarios/scrape/
[[15]]: HTML Scraping

[16]: https://github.com/RonanC/Countdown-Letters-Game-Solver/blob/master/solver/permut.py
[[16]]: permut.py file

[17]: https://github.com/RonanC/Countdown-Letters-Game-Solver/tree/master/solver
[[17]]: solver directory
