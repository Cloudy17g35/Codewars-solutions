'''https://www.codewars.com/kata/51e0007c1f9378fa810002a9'''


def parse(data):
    value = 0
    result = []
    
    for letter in data:
        if letter == 'i':
            value += 1
        
        elif letter  == 'd':
            value -= 1
        
        elif letter == 's':
            value **= 2
            
        elif letter == 'o':
            result.append(value)
            
    return result
