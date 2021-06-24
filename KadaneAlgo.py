"""
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
"""
# Time : O(N)     Space: O(1)
def kadaneAlgorithm(arr):
    maxEnding = arr[0]
    maxSoFar = arr[0]
    for num in arr[1:]:
        maxEnding = max(num, maxEnding + num)
        maxSoFar = max(maxSoFar, maxEnding)
    return maxSoFar

if __name__ == '__main__':
    # arr = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    arr = [5, -4, -2, 6, -1]
    print(kadaneAlgorithm(arr))