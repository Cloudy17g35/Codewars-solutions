'''https://www.codewars.com/kata/5a905c2157c562994900009d'''
import math
def product_array(numbers):

    return [math.prod(numbers[:i] + numbers[i + 1:]) for i in range(len(numbers))]
