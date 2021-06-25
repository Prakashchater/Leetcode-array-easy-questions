def longestConsecutive(arr):
    res = 0
    num_set = set(arr)
    for i in arr:
        if i in num_set:
            num_set.remove(i)
            prev, nxt = i - 1, i + 1
            while prev in num_set:
                num_set.remove(prev)
                prev -= 1
            while nxt in num_set:
                num_set.remove(nxt)
                nxt += 1
            res = max(res, nxt - prev - 1)
    return res
    # ans = 0
    # s = set()
    # for i in arr:
    #     s.add(i)
    # for i in range(len(arr)):
    #     if arr[i] - 1 not in s:
    #         j = arr[i]
    #         while j in s:
    #             j += 1
    #         ans = max(ans, j - arr[i])
    # return ans


if __name__ == '__main__':
    arr = [2,6,1,9,4,5,3]
    print(longestConsecutive(arr))



"""
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
"""