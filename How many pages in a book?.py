def amount_of_pages(summary):
    i = 1
    string = ''
    
    while len(string) != summary:
        string += str(i)
        i += 1
    return i - 1
