'''Get the next prime number!

You will get a numbern (>= 0) and your task is to find the next prime number.

Make sure to optimize your code: there will numbers tested up to about 10^12.'''
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

def next_prime(n):
    
    current_number = n + 1

    while not is_prime(current_number):
        current_number += 1

    return current_number
