'''

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

'''

def valid_parentheses(string):
    stack: list = []
    closing_to_open: dict = {')': '(', ']': '[', '}': '{'}
    parenthesis = ['(', ')', '[', ']', '{', '}']

    for char in string:
        if char not in parenthesis:
            string = string.replace(char, '')

    for char in string:
        if char in closing_to_open:
            if stack and stack[-1] == closing_to_open[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return False if stack else True
