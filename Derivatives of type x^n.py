def differentiate(poly):
    if not 'x' in poly:
        return '0'
    if poly == 'x':
        return '1'
    if poly == '-x':
        return '-1'
    if not '^' in poly:
        return ''.join([d for d in poly if d != 'x'])
    
    else:
        number, exp =  poly.split('^')[0], poly.split('^')[1]
        exp = int(exp)
        number = ''.join([d for d in number if d != 'x'])
        if not number:
            number = 1
        elif number == '-':
            number = -1
        else:
            number = int(number)
        print(number)
        calculation = number * exp
        exp -= 1
        if exp == 1:
            return str(calculation) + 'x'
        else:
            return str(calculation) + 'x^' + str(exp)
