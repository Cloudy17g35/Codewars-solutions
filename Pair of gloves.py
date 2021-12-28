'''https://www.codewars.com/kata/58235a167a8cb37e1a0000db'''

from collections import Counter
def number_of_pairs(gloves):

    return sum([value//2 for value in Counter(gloves).values()])
