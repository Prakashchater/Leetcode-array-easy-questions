def moveEnd(arr, k):
    i = 0
    j = len(arr) - 1
    while i < j:
        while i < j and arr[j] == k:
            j -= 1

        if arr[i] == k:
            arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return arr

if __name__ == '__main__':
    arr = [7, 8, 1, 2, 2, 4, 2, 9]
    k = 2
    print(moveEnd(arr, k))