# Brute Force
# time: O(N^3)        Space: O(1)
"""
def tripletSum(arr, x):
    for i in range(0, len(arr)-2):
        for j in range(i + 1, len(arr)-1):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == x:
                    return True

    return False


if __name__ == '__main__':
    arr = [3, 1, 5, 1, 9, 8]
    x = 16
    print(tripletSum(arr, x))
"""
# time: O(N^2)        Space: O(1)
"""
def tripletSum(arr, x):
    for i in range(0, len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            if arr[i] + arr[left] + arr[right] == x:
                return True
            elif arr[i] + arr[left] + arr[right] < x:
                left += 1
            else:
                right -= 1
    return False

if __name__ == '__main__':
    arr = [3, 1, 5, 1, 9, 8]
    x = 16
    print(tripletSum(arr, x))
"""


# Python3 program to find a triplet using Hashing
# returns true if there is triplet with sum equal
# to 'sum' present in A[]. Also, prints the triplet
def find3Numbers(A, arr_size, sum):
    for i in range(0, arr_size - 1):
        # Find pair in subarray A[i + 1..n-1]
        # with sum equal to sum - A[i]
        s = set()
        curr_sum = sum - A[i]
        for j in range(i + 1, arr_size):
            if (curr_sum - A[j]) in s:
                print("Triplet is", A[i], ", ", A[j], ", ", curr_sum - A[j])
                return True
            s.add(A[j])

    return False


# Driver program to test above function
A = [1, 4, 45, 6, 10, 8]
sum = 22
arr_size = len(A)
find3Numbers(A, arr_size, sum)


