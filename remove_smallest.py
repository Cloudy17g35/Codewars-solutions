def remove_smallest(numbers):
    if len(numbers) > 1:
        new_numbers = numbers
        new_numbers.remove(min(numbers))
        return new_numbers
        
    return []
