def explode(s):
    return ''.join([number * int(number) for number in s])
