def increment_string(string):
    if not string:
        return '1'
    else:
        number = ''.join([n for n in string if n.isnumeric()])
        if not number:
            string += '1'
            return string
        def zeros_count(s):
            number_of_zeros = len([z for z in s if z == '0'])
            other_nums = ''.join([n for n in s if n != '0'])
            return number_of_zeros
        count_of_zeros = zeros_count(string)
        if number.endswith('9'):
            count_of_zeros -= 1
        if count_of_zeros > 1 and set(number) == set('0'):
            count_of_zeros -= 1
        new_number = int(number) + 1
        new_string = string.replace(number, '')
        return new_string +count_of_zeros * '0'+ str(new_number)
