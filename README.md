# Countdown-Letters-Game-Solver
### Student name: Ronan Connolly
#### Student number: G00274374
A Python script that solves the Countdown letters game, and a readme explaining how the solver works.


Insert introduction here.

## Background
The first task I completed as part of this project was to Google "countdown letters game solver".
Google gave me two relevant results on the first page, these are [Cool Project name][2] and [Cool Solver][3].

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
[1]: http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/
[2]: http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/
[3]: http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/
