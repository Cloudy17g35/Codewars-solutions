'''Disarium number is the number that The sum of its digits powered with their respective positions is equal to the number itself.'''


def disarium_number(number):
    return "Disarium !!" if sum([int(str(number)[i]) ** (i + 1) for i in range(len(str(number)))]) == number else "Not !!"

  
