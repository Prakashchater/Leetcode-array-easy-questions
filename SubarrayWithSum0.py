def subArray(arr):
    pre = 0
    s = set()
    for i in range(len(arr)):
        pre += arr[i]

        if pre == 0 or pre in s:
            return True
        s.add(pre)
    return False


if __name__ == '__main__':
    arr = [4, 2, 5, 1, 6]
    print(subArray(arr))