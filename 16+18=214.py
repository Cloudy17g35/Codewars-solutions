def add(num1, num2):
    string_num1 = str(num1)
    string_num2 = str(num2)

    longer, shorter = sorted([string_num1, string_num2], key=len, reverse=True)
    
    if len(longer) == len(shorter):
        return int(''.join([str(int(shorter[i]) + int(longer[i])) for i in range(len(longer))]))
    
    else:
        shorter = (len(longer) - len(shorter)) * '0' + shorter
        return int(''.join([str(int(longer[i]) + int(shorter[i])) for i in range(len(longer))]))
