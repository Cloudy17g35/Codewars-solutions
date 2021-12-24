'''Given an array/list [] of integers , Find the Nth smallest element in this array of integers'''

def nth_smallest(arr, pos):
    return sorted(arr)[pos - 1]
