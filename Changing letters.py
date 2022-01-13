'''When provided with a String, capitalize all vowels

For example:

Input : "Hello World!"

Output : "HEllO WOrld!"

Note: Y is not a vowel in this kata.

'''

def swap(st):
    
    return ''.join([letter.upper() if letter in 'aeiou' else letter for letter in st])
