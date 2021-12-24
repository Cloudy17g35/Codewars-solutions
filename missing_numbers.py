'''You are given an unsorted array containing all the integers from 0 to 100 inclusively. 
However, one number is missing. Write a function to find and return this number'''

def missing_no(nums):
    return list(set(range(0, 101)) - set(nums))[0]
