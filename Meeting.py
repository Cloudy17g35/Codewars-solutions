'''https://www.codewars.com/kata/59df2f8f08c6cec835000012'''


def meeting(s):
    s = s.split(';')


    result = []
    for name_and_surname in s:
        name, surname = name_and_surname.split(':')
        result.append((surname.upper(), name.upper()))

    return ''.join(str(n) for n in sorted(result, key=lambda x: (x[0], x[1]))).replace("'", '')
