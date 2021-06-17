def twoHalf(s):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U']
    c1 = 0
    c2 = 0
    for i in range(len(s)//2):
        if s[i] in vowel:
            c1 += 1
        if s[-i-1] in vowel:
            c2 += 1
    return c1 == c2


if __name__ == '__main__':
    s = "book"
    print(twoHalf(s))