def HeightChecker(arr):
    count = 0
    expected = sorted(arr)
    for i in range(len(arr)):
        if arr[i] != expected[i]:
            count += 1
    return count


if __name__ == '__main__':
    arr = [1,1,4,2,1,3]
    print(HeightChecker(arr))