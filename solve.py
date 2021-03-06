def is_prime(n):

    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    # We store the number of factors in this variable
    factors = 0
    # This will loop from 1 to n
    for i in range(1, n+1):
        # Check if `i` divides `n`, if yes then we increment the factors
        if n % i == 0:
            factors += 1
    # If total factors are exactly 2
    if factors == 2:
        return True
    return False


def solve(a,b):
    factors: list = []
    
    for i in range(1, b + 1):
        
        if b % i == 0:
            factors.append(i)
    prime_factors = [factor for factor in factors if is_prime(factor)]
    
    for factor in prime_factors:
        if a % factor:
            return False
    return True
    
  
