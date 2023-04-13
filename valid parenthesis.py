def isValidParenthesis(s):
    stack = []
    for b in s:
        if b == '(' or b == '[' or b == '{':
            stack.append(c)
        elif len(stack) == 0:
            return False
        elif b == ')' and stack[-1] == '(':
            stack.pop()
        elif b == ']' and stack[-1] == '[':
            stack.pop()
        elif b == '}' and stack[-1] == '{':
            stack.pop()
        else:
            return False
    return len(stack) == 0