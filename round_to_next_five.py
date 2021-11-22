'''Given an integer as input, can you round it to the next (meaning, "higher") multiple of 5?'''

def round_to_next5(n:int) -> int:
    
    while n % 5:
        n += 1
    return n
