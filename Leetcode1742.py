import collections
def MaxLimit(low, high):
    c = collections.Counter()
    def count(x):
        total = 0
        while x > 0:
            total += x % 10
            x //= 10
        # print(total)
        return total


    for i in range(low, high + 1):
        c[count(i)] += 1
    return max(c.values())

if __name__ == '__main__':
    low = 5
    high = 15
    print(MaxLimit(low, high))