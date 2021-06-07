def removeOuterParenthesis(s):
    stack = []
    bal = 0
    for c in s:
        if c == '(' and bal > 0:
            stack.append(c)
        if c == ')' and bal > 1:
            stack.append(c)

        if c == '(':
            bal += 1
        else:
            bal -= 1
    return "".join(stack)

if __name__ == '__main__':
    s = "()(())"
    print(removeOuterParenthesis(s))