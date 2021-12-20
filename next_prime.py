def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True if n >= 2 else False

def next_prime(n):
    current_number = n + 1

    while not is_prime(current_number):
        current_number += 1

    return current_number
