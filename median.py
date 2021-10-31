def median(array):
    return sorted(array)[len(array) // 2] if len(array) % 2 else (sorted(array)[len(array) // 2] + sorted(array)[(len(array) // 2) -1]) / 2
