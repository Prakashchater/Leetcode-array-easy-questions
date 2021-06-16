def replaceDigits(s):
    a = list(s)

    for i in range(1, len(a), 2):
        a[i] = chr(ord(s[i-1]) + int(a[i]))
    return ''.join(a)


if __name__ == '__main__':
    s = "a1b2c3d4e"
    print(replaceDigits(s))