''' You are going to be given a word. Your job will be to make sure that each character in that word has the exact same number of occurrences. You will return true if it is valid, or false if it is not.

For this kata, capitals are considered the same as lowercase letters. Therefore: "A" == "a"

The input is a string (with no spaces) containing [a-z],[A-Z],[0-9] and common symbols. The length will be 0 < length < 100.'''

# here's two approaches of solving this problem

def validate_word(word: str):
    freq_table = {} # this dict will keep number of occurrences of letters

    for char in word.lower():
        if char not in freq_table:
            freq_table[char] = 1
        else:
            freq_table[char] += 1
    print(freq_table)
    return len(set(freq_table.values())) == 1



print(validate_word("abcabcd"))


from collections import Counter
def validate_word(word):
    return len(set(Counter(word.lower()).values())) == 1
