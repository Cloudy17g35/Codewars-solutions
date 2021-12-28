'''https://www.codewars.com/kata/5710a50d336aed828100055a'''

def sc(s):

    i , k = 0, 1
    result = 0


    while k != len(s):
        if s[i] != s[k]:
            result += 7

        else:
            result += 2

        i,k = k, k + 1
        
        
    return result + 1
