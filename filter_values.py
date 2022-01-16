'''In this kata you will create a function that takes a list of 
non-negative integers and strings and returns a new list with the strings filtered out.

'''
def filter_list(l):
    return [e for e in l if not isinstance(e, str)]
