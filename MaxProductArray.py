def maxProductArray(arr):
    maxpro = 1
    curr = 1
    for i in range(len(arr)):
        curr = curr * arr[i]
        if curr > maxpro:
            maxpro = curr
        if curr < 0:
            curr = 0
    return maxpro

if __name__ == '__main__':
    arr = [6, -3, -10, 0, 2]
    print(maxProductArray(arr))