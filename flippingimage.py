def flipping(arr):
    for i in range(len(arr)):
        arr[i] = list(reversed(arr[i]))
        for row in arr:
            for index in range(len(row)):
                row[index] = row[index] ^ 1
    return arr



if __name__ == '__main__':
    arr = [[1, 1, 0], [0, 0, 1], [0, 0, 0]]
    print(flipping(arr))
    # flipping(arr)


