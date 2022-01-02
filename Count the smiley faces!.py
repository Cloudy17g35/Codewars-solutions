
'''https://www.codewars.com/kata/583203e6eb35d7980400002a'''


def count_smileys(arr):
    valid_faces = [':-)', ';-)', ':~)', ';~)',
                  ':D', ';-D', ':-D', ';~D', ':~D',
                  ':)', ';)', ';D']
    
    count = 0
    for face in arr:
        if face in valid_faces:
            count += 1
            
    return count
