def assemble(arr):
    if not arr:
        return ''
    string_length = len(arr[0])
    d = {i:'#' for i in range(string_length)}
    
    for s in arr:
        for i in range(string_length):
            current_letter = s[i]
            if current_letter != '*':
                d[i] = current_letter
                
    return ''.join(letter for i, letter in sorted(d.items()))Assemble string
