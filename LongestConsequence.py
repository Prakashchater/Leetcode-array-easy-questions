# Time: O(N*logN)     Space: O(1)
def longestConsecutive(arr):
    count = 0
    ans = 0
    v = []
    arr.sort()
    v.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            v.append(arr[i])


    for i in range(len(v)):
        if (i > 0 and v[i] == v[i-1] + 1):
            count += 1
        else:
            count = 1

        ans = max(ans, count)
    return ans


if __name__ == '__main__':
    arr = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
    print(longestConsecutive(arr))