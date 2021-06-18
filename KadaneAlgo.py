# Time: O(N)      Space: O(1)
def kadaneAlgo(arr):
    maxsum = 0
    currsum = 0
    for i in range(len(arr)):
        currsum = currsum + arr[i]
        if currsum > maxsum:
            maxsum = currsum

        if currsum < 0:
            currsum = 0
    return maxsum

if __name__ == '__main__':
    arr = [5, -4, -2, 6, -1]
    print(kadaneAlgo(arr))