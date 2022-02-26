def validBraces( s: str) -> bool:
    
        dict = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for letter in s:
            if letter in dict:
                stack.append(letter)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if letter != dict[a]:
                    return False
        return stack == []
