'''https://www.codewars.com/kata/53c945d750fe7094ee00016b'''

def inverseMod(a, m):
    try:
        return pow(a, -1 , m)
    except:
        return None
