def sortSentence(s):
    a = [i[-1] + i[:-1] for i in s.split()]
    a.sort()

    ans = ""
    for i in a:
        ans += i[1:] + ' '
    return ans[:-1]


if __name__ == '__main__':
    s = "is2 sentence4 This1 a3"
    print(sortSentence(s))