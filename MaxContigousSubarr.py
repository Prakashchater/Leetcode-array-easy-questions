# def kadaneAlgo(arr):
#     global_max = 0
#     for i in range(len(arr)+1):
#         for j in range(len(arr)+1):
#             if arr[i:j]:
#                 current_max = sum(arr[i:j])
#                 # print(current_max, arr[i:j])
#                 if current_max > global_max:
#                     global_max = current_max
#     return global_max
#
#
#
# if __name__ == '__main__':
#     arr = [1,12,-5,-6,50,3]
#     print(kadaneAlgo(arr))


def contigousMax(arr, k):
    if len(arr) < k:
        return "invalid"

    res = 0
    for i in range(k):
        res += arr[i]
    # print(res)
    curr_sum = res
    for i in range(k, len(arr)):
        curr_sum += arr[i] - arr[i-k]
        res = max(res, curr_sum)
        temp = res / k
        a = "{:.5f}".format(temp)
    print(float(a))

if __name__ == '__main__':
    arr = [1,12,-5,-6,50,3]
    k = 4
    print(contigousMax(arr,k))