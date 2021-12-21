# Write a function that doubles every second integer in a list starting from the left.

def double_every_other(lst):
    for i in range(1, len(lst), 2):
        if i % 2:
            lst[i] = lst[i] * 2
    return lst

print(double_every_other([-1000,1653,210,0,1]))
