def lucky(arr):
    res = [0] * 501
    for i in arr:
        res[i] += 1
    for i in range(500, 0, -1):
        if res[i] == i:
            return i
    return -1


if __name__ == '__main__':
    arr = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
    print(lucky(arr))
