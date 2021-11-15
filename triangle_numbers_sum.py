from functools import lru_cache

@lru_cache(maxsize=None)
def sum_triangular_numbers(n):
    
    if n <= 0:
        return 0

    sum_of_numbers = 0

    for i in range(1, n + 1) :
        triangle_number = i * (i + 1) / (2)
        sum_of_numbers += triangle_number

    return sum_of_numbers
