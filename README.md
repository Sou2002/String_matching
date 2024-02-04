------README------

@ Overview:


# Purpose of the Code:

The Purpose of the code is to find the closely similar strings & arrange them in an order.
Then write the matching pairs in a pandas dataframe.


# How to run it:

'find_matching.py' is the file where the function that finds the similarity between two strings is written.
The code is very easy to run. Simply just run the 'main.ipynb' notebook file. (Run all the cells)


# Chosen Approach:

The problem of matching closely similar strings was solved using the Levenshtein distance.
There is a library named 'thefuzz' which uses the Levenshtein distance to find the similarity between two strings.
As our given problem has some patterns to match I've chosen the 'token_set_ratio' function from the library, 
that works by sorting the tokens of two strings and then find similarity between them.
