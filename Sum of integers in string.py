import re
def sum_of_integers_in_string(s):
    return sum([int(d) for d in re.findall(re.compile("[0-9]+"), s)])
