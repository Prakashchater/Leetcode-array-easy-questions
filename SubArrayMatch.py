def isSubset(a1, a2):
    s = set()
    for i in range(len(a1)):
        s.add(a1[i])

    p = len(s)
    for i in range(len(a2)):
        s.add(a2[i])

    if len(s) == p:
        return True
    else:
        return False


if __name__ == '__main__':
    a1 = [11, 13, 21, 3, 7]
    a2 = [11, 3, 7, 1]
    print(isSubset(a1, a2))