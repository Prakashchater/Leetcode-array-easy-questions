# TIME:O(N)       SPACE:O(N)
def isValid(s):
    stack = []
    for char in s:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            curr = stack.pop()
            if curr == "(":
                if char != ")":
                    return False
            if curr == "{":
                if char != "}":
                    return False
            if curr == "[":
                if char != "]":
                    return False
    if stack:
        return False
    return True


# Driver Code
if __name__ == "__main__":
    s = "[(){}{}"

    # Function call
    if isValid(s):
        print("Balanced")
    else:
        print("Not Balanced")

