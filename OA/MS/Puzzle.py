from collections import Counter


from itertools import permutations


from collections import defaultdict


import random


import string 

import re 

def replaceQuestionMark(puzzle):
    # find question marks and iterate through all of them 
    for data in re.finditer(r'\?',puzzle):
        # if the question mark is at the start of the string puzzle exclude only the character following it
        print(data)
        if data.span()[0] == 0: 
            excludeChar = puzzle[(data.span()[0]+1):(data.span()[1]+1)]
        # if the question mark is at the end of the string puzzle exclude only the character preceding it
        elif data.span()[1] == len(puzzle):
            excludeChar = puzzle[(data.span()[0]-1):(data.span()[1]-1)]
        # else exclude characters on both the sides of question mark
        else:
            excludeChar = puzzle[(data.span()[0]-1):(data.span()[1]-1)] + puzzle[(data.span()[0]+1):(data.span()[1]+1)]
        # substitute each question mark one by one with random choice of lowercase characters excluding the exclude character
    
        res= re.sub(r'\?',random.choice([i for i in string.ascii_lowercase if i not in excludeChar]),puzzle,count=0)
    return res

# this is the driving code to test the three examples here 
print(replaceQuestionMark('xy?xz?'))
#print(replaceQuestionMark('ab?e?mr??'))
#print(replaceQuestionMark('??????'))


t=random.choice([i for i in string.ascii_lowercase if i not in 'ab'])
print(t)
