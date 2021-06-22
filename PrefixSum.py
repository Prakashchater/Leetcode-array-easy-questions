from itertools import accumulate
def prefixSum(arr):
    return list(accumulate(arr))

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50, 60]
    print(prefixSum(arr))