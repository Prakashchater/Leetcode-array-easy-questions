No_of_chars = 256
def duplicateCount(s):
    count = [0] * No_of_chars
    count = fillChar(s, count)
    k = 0
    for i in count:
        if int(i) > 1:
            print(chr(k)+". count= " + str(i))
        k += 1

def fillChar(s, count):
    for i in s:
        count[ord(i)] += 1
    return count

if __name__ == '__main__':
    s = "geeksforgeeks"
    duplicateCount(s)






# O(N*LogN) Time      O(K) Space
"""
from collections import defaultdict
def duplicateCount(s):
    count = defaultdict(int)
    for i in range(len(s)):
        count[s[i]] += 1

    for i in count:
        if count[i] > 1:
            print(i, ", count= ", count[i])


if __name__ == '__main__':
    s = 'geeksforgeeks'
    duplicateCount(s)
"""

