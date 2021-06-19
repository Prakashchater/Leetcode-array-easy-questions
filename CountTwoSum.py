# Time: O(N^2)        Space:O(1)
def getPairsCount(arr, k):
    # count = 0
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         curr_sum = arr[i] + arr[j]
    #         if k == curr_sum:
    #             count += 1
    # return count
    m = [0] * 1000
    for i in range(0, len(arr)):
        m[arr[i]] += 1
    count = 0
    for i in range(len(arr)):
        count += m[k - arr[i]]
        if k - arr[i] == arr[i]:
            count -= 1
    return int(count/2)



if __name__ == '__main__':
    arr = [1, 1, 1, 1]
    k = 2
    print(getPairsCount(arr, k))