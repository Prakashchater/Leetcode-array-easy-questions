def removeAdjacent(s):
    res = []
    for c in s:
        if res and res[-1] in c:
            res.pop()
        else:
            res.append(c)
    return "".join(res)

if __name__ == '__main__':
    s = "azxxzy"
    print(removeAdjacent(s))