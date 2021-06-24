"""
# Time : O(N^2)     Space: O(1)
def maxProductArray(arr):
    res = arr[0]
    for i in range(0, len(arr)):
        mul = arr[i]
        for j in range(i+1, len(arr)):
            res = max(res, mul)
            mul *= arr[j]

        res = max(res, mul)
    return res

if __name__ == '__main__':
    # arr = [-3, 2, -4, 6, 0, -8, 5]
    arr = [1, -2, -3, 0, 7, -8, -2]
    print(maxProductArray(arr))
"""

# Time : O(N)     Space: O(1)
def maxProductArray(arr):
    maxoverall = arr[0]
    maxEnding = arr[0]
    minEnding = arr[0]
    for i in range(1, len(arr)):
        temp = maxEnding
        maxEnding = max(arr[i], arr[i] * maxEnding, arr[i] * minEnding)
        minEnding = min(arr[i], arr[i] * temp, arr[i] * minEnding)
        maxoverall = max(maxoverall, maxEnding)
    return maxoverall

if __name__ == '__main__':
    arr = [-3, 2, -4, 6, 0, -8, 5]
    print(maxProductArray(arr))