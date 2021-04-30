# time: O(N)   || space:O(N)

def BinarySearch(arr, k):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        pot_match = arr[mid]
        if pot_match == k:
            return pot_match
        elif pot_match > k:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == '__main__':
    arr = [1,2,3,4,5,56,67,7,6,5,4,3,33,32,21,2]
    k = 0
    result = BinarySearch(arr, k)
    if result != -1:
        print("True")
    else:
        print("False")
