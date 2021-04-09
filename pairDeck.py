from collections import Counter


def cards(arr):
    count = Counter(arr)
    n = len(arr)
    for i in range(2,n+1):
        if n % i == 0:
            if all(value % i == 0 for value in count.values()):
                return True

    return False


if __name__ == '__main__':
    arr = [1, 2, 4, 4, 3, 2, 1]
    print(cards(arr))
