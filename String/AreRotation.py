def areRotation(s1, s2):
    if len(s1) != len(s2):
        return 0

    temp = s1 + s1
    if temp.count(s2) > 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    s1 = "abcd"
    s2 = "cdab"
    print(areRotation(s1, s2))


