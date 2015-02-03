Designing a lexical decision experiment
=======================================

Research question: Is visual word recognition influenced by the length in lettters) and the frequency of use? Are short or frequent words more easily recognized than longer or less frequent ones?

We are going setup a lexical decision experiment (in French). In such a experiment, participants read a string of character and have to decide wether it is an actual word or not.

1. Creating the materials (using lexique.org)

2. Programming the experiment (using opensesame)

3. Analysing data (Using R and Rstudio)


Preparation
-----------

The experiment will have two factors (or independent variables, that we, as experimenters, will manipulate):

1. length (4 characters  vs. 6 characters )
2. frequency (low vs. high)

(The dependent variables are going to be lexical decision time and recognition rate) 

### Selection of words


A list of French words and their frequencies and length can be downloaded from http://www.lexique.org, but we are going to use the file `lexique_small.csv`

To decide what are low and high frequencies, we need to explore the distribution of frequencies in the French lexicon.

I will use R.

- Plot an histogram of frequencies (to know more, see about Zipf's law on Wikipedia)
- Plot the relationship between frequency and length 
- Select 4 sets of words (LF4, LF6, HF4, HF6) 

### Creation of pseudowords.

Any suggestion?

We can try and do it ourself in Python.



Stimulation
-----------

Download opensesame from http://osdoc.cogsci.nl
